import wfdb
import numpy as np
import os
import pandas as pd

def load_ecg_record(record_id, dataset='mitdb', **kwargs):
    """
    Dispatcher to load ECG record from PhysioNet or Local CSV.
    """
    if dataset == 'local_646':
        return load_csv_record(record_id, **kwargs)
    else:
        return load_physionet_record(record_id, dataset)

def load_physionet_record(record_id, dataset='mitdb'):
    """Load an ECG record from PhysioNet via wfdb."""
    try:
        record = wfdb.rdrecord(str(record_id), pn_dir=dataset)
        signal = record.p_signal[:, 0]
        fs = record.fs
        
        return {
            'signal': signal,
            'fs': fs,
            'record_name': record.record_name,
            'comments': record.comments
        }
    except Exception as e:
        raise ValueError(f"Failed to load record {record_id} from {dataset}: {e}")

def load_csv_record(file_path, channel='ECG'):
    """
    Load data from the 646_data CSV format (no column names).
    
    Column Mapping:
    - Index 0 (A): Frame Index
    - Index 1 (B): Timestamp 
    - Index 2 (C): PPG
    - Index 3 (D): ECG
    
    Sampling rate: 50 Hz
    """
    try:
        # Check if it's just a filename or a full path
        if not os.path.exists(file_path):
            data_dir = "646_data"
            file_path = os.path.join(data_dir, file_path)
            
        # Read CSV without header
        df = pd.read_csv(file_path, header=None, engine='python', skip_blank_lines=True)
        
        # Smart Column Detection
        # Usually: 0=Index, 1=Time, 2=PPG, 3=ECG
        target_col = None
        
        if channel == 'ECG':
             # Try col 3 first, fallback to 2 or 1 if 3 doesn't exist/is empty
             if df.shape[1] > 3: target_col = 3
             elif df.shape[1] > 1: target_col = 1 # Fallback
        else:
             # PPG usually col 2
             if df.shape[1] > 2: target_col = 2
             elif df.shape[1] > 1: target_col = 1
             
        if target_col is None:
            raise ValueError(f"File structure unknown (cols={df.shape[1]})")

        # Extract signal
        signal = pd.to_numeric(df.iloc[:, target_col], errors='coerce').dropna().values
        
        # Infer Sampling Rate from Timestamp (Col 1) if possible
        fs = 50.0 # Default fallback
        if df.shape[1] > 1:
            try:
                # Assuming Col 1 is timestamp in seconds or ms
                # We take the median difference to be robust against jitter
                timestamps = pd.to_numeric(df.iloc[:, 1], errors='coerce').dropna().values
                if len(timestamps) > 100:
                    diffs = np.diff(timestamps)
                    # Handle if timestamp is in ms vs seconds
                    median_diff = np.median(diffs)
                    if median_diff > 10: # Likely ms (e.g. 20ms = 50Hz)
                         fs = 1000.0 / median_diff
                    elif median_diff > 0: # Likely seconds (e.g. 0.02s = 50Hz)
                         fs = 1.0 / median_diff
                    # Clamp to reasonable range (10Hz - 1000Hz)
                    fs = max(10.0, min(fs, 1000.0))
            except:
                pass # Fallback to 50Hz

        # Remove trailing zeros (empty data)
        non_zero_indices = np.where(signal != 0)[0]
        if len(non_zero_indices) > 0:
            last_index = non_zero_indices[-1]
            signal = signal[:last_index+1]
            
        return {
            'signal': signal.astype(float),
            'fs': float(fs), # Ensure float
            'record_name': f"{os.path.basename(file_path)} ({channel})",
            'comments': [f"Source: Local CSV, Channel: {channel}, Detected FS: {fs:.1f}Hz"]
        }
    except Exception as e:
        raise ValueError(f"Failed to load CSV record ({channel}) from {file_path}: {e}")

if __name__ == "__main__":
    # Test
    try:
        # data = load_ecg_record('100', 'mitdb')
        # print(f"Loaded {data['record_name']}, fs={data['fs']}, samples={len(data['signal'])}")
        pass
    except Exception as e:
        print(e)
