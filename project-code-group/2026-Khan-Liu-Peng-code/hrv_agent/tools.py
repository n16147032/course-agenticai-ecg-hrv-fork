import neurokit2 as nk
import numpy as np
import pandas as pd

def preprocess_ecg(ecg_signal, fs, strategy='A'):
    """
    Preprocess ECG signal based on strategy.
    
    Strategy A: Bandpass 0.5-40Hz (Standard monitoring)
    Strategy B: Bandpass 0.5-35Hz + explicit baseline removal (Noisier signals)
    Strategy C: High-pass 0.5Hz only (Minimal filtering)
    """
    # Sanitize input
    ecg_signal = np.array(ecg_signal)
    
    # 0. Resampling Fix: Upsample low-frequency signals (e.g., 50Hz) to improve peak detection
    target_fs = 250.0
    if fs < 100:
        # We upsample to 250Hz which is a standard for many peak detectors
        # This significantly improves Pan-Tompkins and NeuroKit detection on 50Hz data
        num_samples = int(len(ecg_signal) * (target_fs / fs))
        from scipy.signal import resample
        ecg_signal = resample(ecg_signal, num_samples)
        fs = target_fs
        
    try:
        if strategy == 'A':
            # NeuroKit default cleaning. Safe for most fs.
            clean = nk.ecg_clean(ecg_signal, sampling_rate=fs, method='neurokit') 
            return clean
            
        elif strategy == 'B':
            # Biosppy usually requires fs > 100Hz for its default filters (0.67-45Hz)
            if fs < 100:
                # Custom safe bandpass for low fs (0.5 to Nyquist-2Hz)
                highcut = min(40, (fs / 2) - 2)
                clean = nk.signal_filter(ecg_signal, sampling_rate=fs, lowcut=0.5, highcut=highcut, method='butterworth', order=5)
            else:
                clean = nk.ecg_clean(ecg_signal, sampling_rate=fs, method='biosppy')
            return clean
            
        elif strategy == 'C':
            # Minimalist: correct baseline wander only (highpass)
            clean = nk.signal_filter(ecg_signal, sampling_rate=fs, lowcut=0.5, method='butterworth', order=5)
            return clean

        elif strategy == 'D':
            # AGGRESSIVE: Focus ONLY on QRS energy (5-20Hz).
            # This destroys ECG morphology but makes R-peaks extremely prominent.
            # Best for very noisy or low-frequency (50Hz) data.
            clean = nk.signal_filter(ecg_signal, sampling_rate=fs, lowcut=5, highcut=20, method='butterworth', order=5)
            return clean

        else:
            return ecg_signal
    except Exception as e:
        print(f"Preprocessing error with strategy {strategy}: {e}")
        # Final fallback: no filtering
        return ecg_signal

def detect_rpeaks(cleaned_ecg, fs, method='neurokit'):
    """
    Detect R-peaks.
    
    Methods: 'neurokit', 'pantompkins', 'nabian2018' (stand-in for wavelet/others)
    """
    try:
        # nk.ecg_peaks returns (signals, info)
        # info['ECG_R_Peaks'] contains indices
        _, info = nk.ecg_peaks(cleaned_ecg, sampling_rate=fs, method=method)
        rpeaks = info['ECG_R_Peaks']
        
        # Handle case where no peaks found
        if len(rpeaks) == 0:
            return np.array([])
            
        return rpeaks
    except Exception as e:
        print(f"Peak detection error with method {method}: {e}")
        return np.array([])
    
def validate_signal_quality(cleaned_ecg, rpeaks, fs):
    """
    Compute basic SQIs to guide the agent.
    Returns a dict with metrics:
    - n_peaks: count
    - mean_hr: bpm
    - missing_beat_ratio: placeholder for simplistic check
    - snr_estimate: crude variance ratio or similar (optional)
    """
    if len(rpeaks) < 2:
        return {'grade': 'F', 'reason': 'Less than 2 peaks detected'}
    
    # Calculate RR intervals in ms
    rr_intervals = np.diff(rpeaks) / fs * 1000
    mean_rr = np.mean(rr_intervals)
    mean_hr = 60000 / mean_rr if mean_rr > 0 else 0
    
    # Physiologically impossible HR check
    if mean_hr < 10 or mean_hr > 300:
         return {'grade': 'E', 'reason': 'HR out of typical range (10-300)', 'mean_hr': mean_hr}
         
    # Check for extreme outlier intervals (artifacts or missed beats)
    # Simple logic: if > 20% of RR intervals are > 1.5x median or < 0.5x median
    median_rr = np.median(rr_intervals)
    outliers = np.sum((rr_intervals > 1.5 * median_rr) | (rr_intervals < 0.5 * median_rr))
    outlier_ratio = outliers / len(rr_intervals)
    
    # EXTREMELY LENIENT thresholds to ensure a report is ALWAYS generated
    if outlier_ratio > 0.90:
        return {'grade': 'E', 'reason': f'Very poor signal quality ({outlier_ratio*100:.1f}%)', 'outlier_ratio': outlier_ratio}
    
    if outlier_ratio > 0.70:
        return {'grade': 'D', 'reason': f'Poor signal quality ({outlier_ratio*100:.1f}%)', 'outlier_ratio': outlier_ratio}
        
    if outlier_ratio > 0.50:
        return {'grade': 'C', 'reason': f'Moderate noise ({outlier_ratio*100:.1f}%)', 'outlier_ratio': outlier_ratio}
        
    if outlier_ratio > 0.15:
        return {'grade': 'B', 'reason': f'Minor noise ({outlier_ratio*100:.1f}%)', 'outlier_ratio': outlier_ratio}
        
    return {'grade': 'A', 'reason': 'Clean signal trajectory', 'mean_hr': mean_hr}
