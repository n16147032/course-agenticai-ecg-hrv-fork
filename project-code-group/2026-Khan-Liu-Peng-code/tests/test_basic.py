import pytest
import numpy as np
import neurokit2 as nk
from hrv_agent.tools import preprocess_ecg, detect_rpeaks

def test_preprocess_shape():
    # Synthetic float signal
    ecg = nk.ecg_simulate(duration=5, sampling_rate=250)
    cleaned = preprocess_ecg(ecg, 250, strategy='A')
    assert len(cleaned) == len(ecg), "Output length must match input"
    assert isinstance(cleaned, np.ndarray)

def test_preprocess_strategies():
    ecg = nk.ecg_simulate(duration=2, sampling_rate=250)
    # Just check they don't crash
    preprocess_ecg(ecg, 250, strategy='B')
    preprocess_ecg(ecg, 250, strategy='C')

def test_peak_detection():
    # Known signal with 60 bpm = 1 beat/sec => in 10s expect ~10 beats
    ecg = nk.ecg_simulate(duration=10, heart_rate=60, sampling_rate=250)
    cleaned = preprocess_ecg(ecg, 250, strategy='A')
    peaks = detect_rpeaks(cleaned, 250, method='neurokit')
    
    # Allow +/- 1 beat tolerance
    assert 9 <= len(peaks) <= 11, f"Expected ~10 peaks, got {len(peaks)}"
