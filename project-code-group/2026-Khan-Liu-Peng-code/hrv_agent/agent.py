from .data import load_ecg_record
from .tools import preprocess_ecg, detect_rpeaks, validate_signal_quality
from .metrics import compute_hrv_metrics
from .plotting import plot_results
from .report import generate_markdown_report
import os
import json
import logging

class HRVCoachAgent:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = self._setup_logger()
        
    def _setup_logger(self):
        logger = logging.getLogger("HRVAgent")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        return logger

    def run(self, record_id, dataset='mitdb', **kwargs):
        self.logger.info(f"Starting run for Record {record_id} from {dataset}")
        
        # 1. Sense: Load Data
        try:
            data = load_ecg_record(record_id, dataset, **kwargs)
            ecg = data['signal']
            fs = data['fs']
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            return {"grade": "Reject", "reason": f"Load failure: {e}"}

        # Defined Strategies to Try
        # Order: 
        # 1. Standard (Strategy A, Neurokit)
        # 2. Stronger Filter (Strategy B, Neurokit) 
        # 3. Robust Detection (Strategy A, Pantompkins -- usually good for noise)
        strategies = [
            {'name': 'Standard', 'preprocess': 'A', 'detector': 'neurokit'},
            {'name': 'StrongFilter', 'preprocess': 'B', 'detector': 'neurokit'},
            {'name': 'RobustDetect', 'preprocess': 'A', 'detector': 'pantompkins'},
        ]
        
        history = []
        best_result = None
        
        # Policy Loop
        for i, policy in enumerate(strategies):
            self.logger.info(f"Attempt {i+1}: Trying {policy['name']} (Pre: {policy['preprocess']}, Det: {policy['detector']})")
            
            # Act
            clean_ecg = preprocess_ecg(ecg, fs, strategy=policy['preprocess'])
            rpeaks = detect_rpeaks(clean_ecg, fs, method=policy['detector'])
            
            # Verify / Quality Check
            quality = validate_signal_quality(clean_ecg, rpeaks, fs)
            
            log_entry = {
                'step': i+1,
                'strategy': policy['preprocess'],
                'method': policy['detector'],
                'grade': quality['grade'],
                'reason': quality['reason'],
                'metrics': quality
            }
            history.append(log_entry)
            
            self.logger.info(f"Validation Result: Grade {quality['grade']} - {quality['reason']}")
            
            # Decision Logic
            if quality['grade'] == 'A':
                # Excellent result, stop early
                best_result = {
                    'ecg': ecg, 'clean_ecg': clean_ecg, 'rpeaks': rpeaks, 'fs': fs,
                    'grade': 'A', 'reason': quality['reason'], 'strategy_used': policy['name'],
                    'preprocess': policy['preprocess'], 'detector': policy['detector']
                }
                break
            
            if quality['grade'] == 'B':
                # Acceptable, but keep it as candidate if we don't find an A later.
                # However, for this simple logic, let's say B is good enough to stop if strictly satisfying.
                # Or we can continue to see if we get an A. Let's start by storing it.
                if best_result is None or best_result['grade'] not in ['A']:
                    best_result = {
                        'ecg': ecg, 'clean_ecg': clean_ecg, 'rpeaks': rpeaks, 'fs': fs,
                        'grade': 'B', 'reason': quality['reason'], 'strategy_used': policy['name'],
                        'preprocess': policy['preprocess'], 'detector': policy['detector']
                    }
            
            # If D or F, continue to next strategy (retry)
            
        # Final Decision
        if best_result is None:
            # All failed or only D/F found. Use the last one or the "least bad" one?
            # Let's assume the last one is the fallback if nothing good was found, 
            # but ideally we pick the best of the bad bunch (e.g. highest SNR or whatever).
            # For simplicity, we Reject if no A or B found.
             self.logger.warning("All strategies failed to produce High Quality (A/B) results.")
             best_result = {
                 'ecg': ecg, 'clean_ecg': clean_ecg, 'rpeaks': rpeaks, 'fs': fs,
                 'grade': 'Reject', 'reason': 'All strategies yielded poor quality',
                 'strategy_used': 'Exhausted',
                 'preprocess': policy['preprocess'], 'detector': policy['detector']
             }
        
        best_result['history'] = history
        
        # Post-Processing: Compute Metrics & Report
        hrv_metrics = {}
        if best_result['grade'] != 'Reject':
            hrv_metrics = compute_hrv_metrics(best_result['rpeaks'], best_result['fs'])
            
            # Plot
            plot_path = os.path.join(self.output_dir, "plots.png")
            signal_type = kwargs.get('channel', 'ECG')
            plot_results(best_result['ecg'], best_result['clean_ecg'], 
                        best_result['rpeaks'], best_result['fs'], 
                        output_path=plot_path, signal_type=signal_type)
            
            # Report
            config = {'record_id': record_id, 'dataset': dataset}
            report_path = generate_markdown_report(best_result, hrv_metrics, config, self.output_dir, run_id=f"{record_id}_{dataset}")
            self.logger.info(f"Report generated at {report_path}")
            
        # Write Agent Log
        with open(os.path.join(self.output_dir, "agent_log.json"), 'w') as f:
            # Can't serialize numpy arrays easily, so exclude large data
            log_dump = {k: v for k, v in best_result.items() if k not in ['ecg', 'clean_ecg', 'rpeaks']}
            log_dump['metrics'] = hrv_metrics
            json.dump(log_dump, f, indent=2)

        return best_result
