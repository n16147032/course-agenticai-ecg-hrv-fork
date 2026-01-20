import openai
import numpy as np
import json
import logging
import os
from .config import Config
from .prompts import *
from .data import load_ecg_record
from .tools import preprocess_ecg, detect_rpeaks, validate_signal_quality
from .metrics import compute_hrv_metrics
from .plotting import plot_results

class OpenRouterHRVAgent:
    """LLM-powered HRV analysis agent using OpenRouter (OpenAI-compatible)"""
    
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = self._setup_logger()
        
        api_key = Config.get_openrouter_key()
        if not api_key:
            raise ValueError("OpenRouter API Key not found. Please set it in .env or the Dashboard UI.")
        
        base_url = os.getenv('OPENROUTER_BASE_URL', Config.OPENROUTER_BASE_URL)
        
        # OpenRouter headers for visibility
        extra_headers = {
            "HTTP-Referer": "https://github.com/google/hrv-coach-agent",
            "X-Title": "HRV Coach Pro v2.1",
        }

        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url,
            default_headers=extra_headers
        )
        self.logger.info(f"Initialized OpenRouter client with base_url: {base_url}")
        
    def _setup_logger(self):
        logger = logging.getLogger("OpenRouterHRVAgent")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        return logger
    
    def _get_signal_stats(self, ecg, fs):
        """Compute basic signal statistics for AI"""
        return {
            'fs': fs,
            'duration': len(ecg) / fs,
            'mean_amp': float(np.mean(ecg)),
            'std_amp': float(np.std(ecg)),
            'baseline_wander': float(np.std(np.convolve(ecg, np.ones(int(fs)), mode='same')))
        }
    
    def _ask_ai(self, prompt):
        """Send prompt to OpenRouter and get response"""
        model = Config.OPENROUTER_MODEL
        try:
            self.logger.info(f"Sending request to OpenRouter (Model: {model})...")
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_OUTPUT_TOKENS
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"OpenRouter API connection failed: {str(e)}")
            return None
    
    def run(self, record_id, dataset='mitdb', **kwargs):
        """Run LLM-powered HRV analysis using OpenRouter"""
        self.logger.info(f"🤖 Starting OpenRouter-powered analysis for Record {record_id}")
        
        # 1. Load Data
        try:
            data = load_ecg_record(record_id, dataset, **kwargs)
            ecg = data['signal']
            fs = data['fs']
            self.logger.info(f"Loaded {len(ecg)} samples at {fs} Hz")
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            return {"grade": "Reject", "reason": f"Load failure: {e}"}
        
        # 2. Get signal statistics
        stats = self._get_signal_stats(ecg, fs)
        
        # 3. Processing loop
        history = []
        best_result = None
        max_attempts = 4
        
        strategies = ['A', 'B', 'C', 'D']
        detectors = ['neurokit', 'pantompkins', 'neurokit', 'pantompkins']
        
        for attempt in range(max_attempts):
            strategy = strategies[attempt]
            detector = detectors[attempt]
            
            self.logger.info(f"Attempt {attempt + 1}: Strategy {strategy}, Detector {detector}")
            
            try:
                clean_ecg = preprocess_ecg(ecg, fs, strategy=strategy)
                rpeaks = detect_rpeaks(clean_ecg, fs, method=detector)
                quality = validate_signal_quality(clean_ecg, rpeaks, fs)
                
                log_entry = {
                    'attempt': attempt + 1,
                    'strategy': strategy,
                    'detector': detector,
                    'grade': quality['grade'],
                    'reason': quality['reason']
                }
                history.append(log_entry)
                
                self.logger.info(f"Result: Grade {quality['grade']} - {quality['reason']}")
                
                if quality['grade'] in ['A', 'B', 'C', 'D', 'E']:  # Accept ALL grades including E
                    best_result = {
                        'ecg': ecg, 'clean_ecg': clean_ecg, 'rpeaks': rpeaks, 'fs': fs,
                        'grade': quality['grade'], 'reason': quality['reason'],
                        'strategy_used': strategy, 'detector': detector,
                        'original_fs': data['fs']
                    }
                    if quality['grade'] == 'A':
                        break
            except Exception as e:
                self.logger.error(f"Processing error in attempt {attempt+1}: {e}")
                continue
                
        if not best_result:
            best_result = {
                'ecg': ecg, 'clean_ecg': clean_ecg if 'clean_ecg' in locals() else ecg,
                'rpeaks': rpeaks if 'rpeaks' in locals() else np.array([]),
                'fs': fs,
                'grade': 'E', 'reason': 'Low quality but forced to complete',
                'strategy_used': strategies[-1], 'detector': detectors[-1],
                'original_fs': data['fs']
            }
            
        best_result['history'] = history
        
        # 4. Compute metrics and Plot
        hrv_metrics = {}
        if best_result['grade'] != 'Reject':
            hrv_metrics = compute_hrv_metrics(best_result['rpeaks'], best_result['fs'])
            
            plot_path = os.path.join(self.output_dir, "plots.png")
            signal_type = kwargs.get('channel', 'ECG')
            plot_results(best_result['ecg'], best_result['clean_ecg'], 
                        best_result['rpeaks'], best_result['fs'], 
                        output_path=plot_path, signal_type=signal_type)
        
        # 5. Generate OpenRouter-powered clinical report
        report_path = os.path.join(self.output_dir, "gemini_report.md") # Legacy filename for UI compatibility
        
        if os.path.exists(report_path) and os.path.getsize(report_path) > 500:
             self.logger.info("♻️ Report exists. Skipping AI call.")
             return best_result

        self.logger.info("📝 Generating report with OpenRouter...")
        
        if hrv_metrics is None: hrv_metrics = {}
        
        report_prompt = CLINICAL_REPORT_PROMPT.format(
            record_id=record_id,
            dataset=dataset,
            grade=best_result['grade'],
            strategy=best_result['strategy_used'],
            detector=best_result['detector'],
            history=json.dumps(history, indent=2),
            mean_nn=f"{hrv_metrics.get('mean_nn', 'N/A'):.1f}" if isinstance(hrv_metrics.get('mean_nn'), (int, float)) else 'N/A',
            sdnn=f"{hrv_metrics.get('sdnn', 'N/A'):.1f}" if isinstance(hrv_metrics.get('sdnn'), (int, float)) else 'N/A',
            rmssd=f"{hrv_metrics.get('rmssd', 'N/A'):.1f}" if isinstance(hrv_metrics.get('rmssd'), (int, float)) else 'N/A',
            pnn50=f"{hrv_metrics.get('pnn50', 'N/A'):.1f}" if isinstance(hrv_metrics.get('pnn50'), (int, float)) else 'N/A',
            lf_power=f"{hrv_metrics.get('lf_power', 'N/A'):.1f}" if isinstance(hrv_metrics.get('lf_power'), (int, float)) else 'N/A',
            hf_power=f"{hrv_metrics.get('hf_power', 'N/A'):.1f}" if isinstance(hrv_metrics.get('hf_power'), (int, float)) else 'N/A',
            lf_hf_ratio=f"{hrv_metrics.get('lf_hf_ratio', 'N/A'):.2f}" if isinstance(hrv_metrics.get('lf_hf_ratio'), (int, float)) else 'N/A'
        )
        
        clinical_report = self._ask_ai(report_prompt)
        provider_name = os.getenv('OPENROUTER_MODEL', Config.OPENROUTER_MODEL)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# 🧬 **HRV Analysis Summary (Powered by {provider_name})**\n\n")
            if clinical_report:
                f.write(clinical_report)
            else:
                f.write("> [!CAUTION]\n")
                f.write("> OpenRouter API Error. Using Rule-Based Summary.\n\n")
                self._write_rule_based_report(f, record_id, best_result, hrv_metrics)
                
        # Save logs
        with open(os.path.join(self.output_dir, "gemini_log.json"), 'w') as f:
            log_data = {
                'record_id': record_id,
                'dataset': dataset,
                'grade': best_result['grade'],
                'strategy': best_result['strategy_used'],
                'detector': best_result['detector'],
                'history': history,
                'metrics': hrv_metrics,
                'ai_provider': provider_name
            }
            json.dump(log_data, f, indent=2)
            
        return best_result

    def _write_rule_based_report(self, f, record_id, best_result, hrv_metrics):
        """Reused rule-based report logic"""
        if hrv_metrics:
            sdnn = hrv_metrics.get('sdnn', 0)
            rmssd = hrv_metrics.get('rmssd', 0)
            ratio = hrv_metrics.get('lf_hf_ratio', 1)
            
            f.write(f"## 📊 Clinical Executive Summary\n")
            if sdnn > 50: overall = "robust physiological state"
            elif sdnn > 20: overall = "moderate stress"
            else: overall = "autonomic suppression"
                
            f.write(f"The analysis for record **{record_id}** indicates **{overall}**.\n\n")
            f.write(f"## 🩺 Key Physiological Insights\n")
            f.write(f"- **Vagal Tone**: RMSSD of **{rmssd:.1f}ms**.\n")
            f.write(f"- **Balance**: Ratio of **{ratio:.2f}**.\n")
            f.write(f"\n## 🛠️ Signal Integrity\n")
            f.write(f"Grade **{best_result['grade']}** via `{best_result['strategy_used']}`.\n")
