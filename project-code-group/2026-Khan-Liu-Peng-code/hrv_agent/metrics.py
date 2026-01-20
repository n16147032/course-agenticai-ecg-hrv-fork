import neurokit2 as nk
import pandas as pd
import numpy as np

def compute_hrv_metrics(rpeaks, fs):
    """
    Compute Time and Frequency domain HRV metrics.
    """
    try:
        # NeuroKit2 can compute HRV directly from peaks
        # usage: nk.hrv(peaks, sampling_rate=fs, show=False)
        
        # We process separately to be safe and handle errors gracefully
        hrv_df = nk.hrv(rpeaks, sampling_rate=fs, show=False)
        
        # Extract relevant columns
        # Time: HRV_MeanNN, HRV_SDNN, HRV_RMSSD, HRV_pNN50
        # Freq: HRV_LF, HRV_HF, HRV_LFHF (usually Welch by default in newer NK versions)
        
        metrics = {}
        
        col_map = {
            'HRV_MeanNN': 'mean_nn',
            'HRV_SDNN': 'sdnn',
            'HRV_RMSSD': 'rmssd',
            'HRV_pNN50': 'pnn50',
            'HRV_LF': 'lf_power',
            'HRV_HF': 'hf_power',
            'HRV_LFHF': 'lf_hf_ratio'
        }
        
        for nk_col, my_col in col_map.items():
            if nk_col in hrv_df.columns:
                val = hrv_df.iloc[0][nk_col]
                if pd.isna(val):
                    metrics[my_col] = None
                else:
                    metrics[my_col] = float(val)
            else:
                metrics[my_col] = None
        
        # Calculate Mean Heart Rate if MeanNN is available
        if metrics.get('mean_nn'):
            metrics['mean_hr'] = 60000.0 / metrics['mean_nn']
        else:
            metrics['mean_hr'] = None
        
        # Add validity check
        # If signal is too short (< 2 min), LF/HF might not be valid/computed by some methods,
        # but NK usually tries.
        
        return metrics
        
    except Exception as e:
        print(f"HRV Computation error: {e}")
        return None
