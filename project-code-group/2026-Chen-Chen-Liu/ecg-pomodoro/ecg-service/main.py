<<<<<<< HEAD
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import numpy as np
import neurokit2 as nk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import (
    EcgSegment,
    EcgFeatures,
    QualityInfo,
    RPeaksInfo,
    HrvTimeInfo,
    PomodoroWorkRequest,
    PomodoroWorkSummary,
    TrendPoint,
    RrSummary,
    HrSummary,
)

APP_ORIGINS = ["http://localhost:3000"]

# Pragmatic robustness thresholds (not medical rules).
MIN_SAMPLES_FOR_PROCESS = 2_000
MIN_RPEAKS_FOR_HRV = 3

app = FastAPI(title="ECG Service", version="1.1.0")
=======
import os
import json
import time
import threading
from datetime import datetime
from typing import List, Dict, Optional

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import wfdb
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from models import EcgSegment, EcgFeatures, BioStatus, UserBaseline, PomodoroSummary

# Configuration
STORAGE_DIR = "data"
os.makedirs(STORAGE_DIR, exist_ok=True)
BIO_STATUS_FILE = os.path.join(STORAGE_DIR, "bio_status.json")
BASELINE_FILE = os.path.join(STORAGE_DIR, "user_baseline.json")
SUMMARY_FILE = os.path.join(STORAGE_DIR, "pomodoro_summary.json")

APP_ORIGINS = ["http://localhost:3000"]
app = FastAPI(title="ECG Service", version="1.0.0")
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9

app.add_middleware(
    CORSMiddleware,
    allow_origins=APP_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state for background tasks
processing_active = True

def get_mit_bih_data(record_name='100', sampto=3000):
    """Fetch MIT-BIH data for simulation."""
    try:
        record = wfdb.rdrecord(record_name, pn_dir='mitdb', sampto=sampto)
        return record.p_signal[:, 0], record.fs
    except Exception as e:
        print(f"Error fetching MIT-BIH data: {e}")
        # Return dummy sine wave if fail
        fs = 360
        t = np.linspace(0, sampto/fs, sampto)
        return 0.5 * np.sin(2 * np.pi * 1.2 * t) + 0.2 * np.random.randn(sampto), fs

def process_ecg(raw_signal: np.ndarray, fs: int):
    """
    Complete ECG processing pipeline:
    detrend -> filter -> smooth -> R peaks -> P/T/QRS -> Metrics -> Plot
    """
    # 1. Detrend and Filter (0.5 - 45 Hz)
    detrended = signal.detrend(raw_signal)
    b, a = signal.butter(3, [0.5, 45], btype='bandpass', fs=fs)
    filtered = signal.filtfilt(b, a, detrended)
    
    # 2. Smooth
    window_len = int(fs * 0.05)
    if window_len % 2 == 0: window_len += 1
    smoothed = signal.savgol_filter(filtered, window_len, 3)
    
    # 3. Find R peaks (using a simple threshold + distance method)
    # Refined: Use squared derivative for QRS detection (Pan-Tompkins like)
    diff = np.diff(smoothed)
    squared = diff ** 2
    # Moving average
    ma_len = int(fs * 0.12)
    integrated = np.convolve(squared, np.ones(ma_len)/ma_len, mode='same')
    
    peaks, _ = signal.find_peaks(integrated, distance=int(fs * 0.6), height=np.mean(integrated)*2)
    
    # 4. P-wave, T-wave, QRS complex extraction
    # Simplified search windows relative to R-peak
    p_waves = [] # List of (start, end) indices
    t_waves = []
    qrs_complexes = []
    
    rr_intervals = []
    
    for i in range(1, len(peaks) - 1):
        r = peaks[i]
        rr_intervals.append((peaks[i] - peaks[i-1]) / fs * 1000.0) # ms
        
        # QRS: simple window
        qrs_start = r - int(fs * 0.05)
        qrs_end = r + int(fs * 0.05)
        qrs_complexes.append((qrs_start, qrs_end))
        
        # T-wave: search after QRS
        t_search_start = r + int(fs * 0.1)
        t_search_end = r + int(fs * 0.4)
        if t_search_end < len(smoothed):
            t_peak_idx = np.argmax(smoothed[t_search_start:t_search_end]) + t_search_start
            t_waves.append((t_peak_idx - int(fs*0.05), t_peak_idx + int(fs*0.05)))
            
        # P-wave: search before QRS
        p_search_start = r - int(fs * 0.25)
        p_search_end = r - int(fs * 0.08)
        if p_search_start > 0:
            p_peak_idx = np.argmax(smoothed[p_search_start:p_search_end]) + p_search_start
            p_waves.append((p_peak_idx - int(fs*0.03), p_peak_idx + int(fs*0.03)))

    # Metrics
    hr = 0.0
    sdnn = 0.0
    if len(rr_intervals) > 1:
        hr = 60000.0 / np.mean(rr_intervals)
        sdnn = np.std(rr_intervals)
        
    return {
        "raw": raw_signal,
        "cleaned": smoothed,
        "peaks": peaks,
        "p_waves": p_waves,
        "t_waves": t_waves,
        "qrs": qrs_complexes,
        "hr_bpm": hr,
        "sdnn_ms": sdnn,
        "rr_ms": rr_intervals
    }

def generate_vis(data, fs, filename="ecg_plot.png"):
    """Generate plotting with annotations."""
    plt.figure(figsize=(12, 6))
    time_ax = np.arange(len(data['raw'])) / fs
    
    plt.subplot(2, 1, 1)
    plt.plot(time_ax, data['raw'], label='Raw ECG', alpha=0.5)
    plt.title("Raw Signal")
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time_ax, data['cleaned'], color='black', label='Cleaned')
    
    # R peaks
    plt.scatter(data['peaks'] / fs, data['cleaned'][data['peaks']], color='red', marker='v', label='R Peak')
    
    # P waves (Blue boxes)
    for start, end in data['p_waves']:
        plt.axvspan(start / fs, end / fs, color='blue', alpha=0.2, label='P wave' if start == data['p_waves'][0][0] else "")
        
    # T waves (Green boxes)
    for start, end in data['t_waves']:
        plt.axvspan(start / fs, end / fs, color='green', alpha=0.2, label='T wave' if start == data['t_waves'][0][0] else "")
        
    plt.title("Cleaned Signal with Features")
    plt.legend()
    plt.tight_layout()
    path = os.path.join(STORAGE_DIR, filename)
    plt.savefig(path)
    plt.close()
    return path

# --- Background Task Implementation ---

def bio_status_loop():
    """High-frequency update to bio_status.json."""
    global processing_active
    while processing_active:
        try:
            # Simulate real-time processing
            raw, fs = get_mit_bih_data(sampto=360*5) # Default fs=360 for MITDB
            res = process_ecg(raw, fs)
            
            status = BioStatus(
                timestamp_ms=int(time.time() * 1000),
                hr_bpm=round(res['hr_bpm'], 2),
                hrv_sdnn_ms=round(res['sdnn_ms'], 2),
                signal_quality_score=1.0, # Placeholder
                is_stressed=res['sdnn_ms'] < 50.0 # Simple heuristic
            )
            
            with open(BIO_STATUS_FILE, "w") as f:
                json.dump(status.dict(), f)
        except Exception as e:
            print(f"Error in bio_status_loop: {e}")
            
        time.sleep(1) # Frequency: 1Hz

def maintain_baseline():
    """Hourly task to maintain user_baseline.json."""
    while processing_active:
        try:
            raw, fs = get_mit_bih_data(sampto=360*60) # 1 minute for baseline
            res = process_ecg(raw, fs)
            
            baseline = UserBaseline(
                user_id="demo_user",
                period_start_hour=datetime.now().hour,
                avg_hr=round(res['hr_bpm'], 2),
                avg_sdnn=round(res['sdnn_ms'], 2),
                last_updated=int(time.time())
            )
            
            with open(BASELINE_FILE, "w") as f:
                json.dump(baseline.dict(), f)
        except Exception as e:
            print(f"Error in maintain_baseline: {e}")
            
        time.sleep(3600) # Hourly

# Start background threads
threads = []
t1 = threading.Thread(target=bio_status_loop, daemon=True)
t2 = threading.Thread(target=maintain_baseline, daemon=True)
t1.start()
t2.start()
threads.extend([t1, t2])

@app.on_event("shutdown")
def shutdown_event():
    global processing_active
    processing_active = False

@dataclass(frozen=True)
class _QualityReport:
    signal_ok: bool
    missing_ratio: float
    quality_index_mean: float
    notes: List[str]


def _to_2d_array(samples: List[List[float]]) -> np.ndarray:
    arr = np.asarray(samples, dtype=float)
    if arr.ndim != 2:
        raise ValueError("samples must be a 2D array with shape [N, C].")
    if arr.shape[0] == 0 or arr.shape[1] == 0:
        raise ValueError("samples is empty.")
    return arr


def _select_primary_channel(samples_2d: np.ndarray, channel_index: int = 0) -> np.ndarray:
    if channel_index < 0 or channel_index >= samples_2d.shape[1]:
        raise ValueError(f"Invalid channel_index={channel_index}.")
    return samples_2d[:, channel_index]


def _missing_ratio(x: np.ndarray) -> float:
    if x.size == 0:
        return 1.0
    bad = ~np.isfinite(x)
    return float(np.sum(bad)) / float(x.size)


def _clean_ecg(x: np.ndarray, sampling_rate_hz: int) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)):
        idx = np.arange(x.size)
        good = np.isfinite(x)
        if np.sum(good) < 2:
            raise ValueError("Too many non-finite samples to interpolate.")
        x = np.interp(idx, idx[good], x[good])
    return nk.ecg_clean(x, sampling_rate=sampling_rate_hz)


def _compute_quality(ecg_cleaned: np.ndarray, sampling_rate_hz: int) -> np.ndarray:
    return nk.ecg_quality(ecg_cleaned, sampling_rate=sampling_rate_hz)


def _detect_rpeaks(ecg_cleaned: np.ndarray, sampling_rate_hz: int) -> np.ndarray:
    _, rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=sampling_rate_hz)
    return np.asarray(rpeaks["ECG_R_Peaks"], dtype=int)


def _rr_intervals_ms(rpeaks_idx: np.ndarray, sampling_rate_hz: int) -> np.ndarray:
    if rpeaks_idx.size < 2:
        return np.asarray([], dtype=float)
    rr_samples = np.diff(rpeaks_idx).astype(float)
    return rr_samples / float(sampling_rate_hz) * 1000.0


def _hrv_from_rr(rr_ms: np.ndarray) -> HrvTimeInfo:
    if rr_ms.size < 2:
        return HrvTimeInfo(mean_hr_bpm=0.0, rmssd_ms=0.0, sdnn_ms=0.0)

    mean_rr = float(np.mean(rr_ms))
    mean_hr = 60000.0 / mean_rr if mean_rr > 0 else 0.0

    sdnn = float(np.std(rr_ms, ddof=0))
    diff_rr = np.diff(rr_ms)
    rmssd = float(np.sqrt(np.mean(diff_rr**2))) if diff_rr.size else 0.0

    return HrvTimeInfo(mean_hr_bpm=round(mean_hr, 2), rmssd_ms=round(rmssd, 2), sdnn_ms=round(sdnn, 2))


def _rr_summary(rr_ms: np.ndarray) -> RrSummary:
    if rr_ms.size == 0:
        return RrSummary()

    med = float(np.median(rr_ms))
    if med <= 0:
        outlier_ratio = 0.0
    else:
        outlier_ratio = float(np.mean(np.abs(rr_ms - med) / med > 0.2))

    return RrSummary(
        n=int(rr_ms.size),
        mean_ms=round(float(np.mean(rr_ms)), 2),
        std_ms=round(float(np.std(rr_ms, ddof=0)), 2),
        min_ms=round(float(np.min(rr_ms)), 2),
        max_ms=round(float(np.max(rr_ms)), 2),
        outlier_ratio=round(outlier_ratio, 3),
    )


def _process_segment(segment: EcgSegment) -> Tuple[_QualityReport, RPeaksInfo, HrvTimeInfo, np.ndarray]:
    samples_2d = _to_2d_array(segment.samples)
    ecg_raw = _select_primary_channel(samples_2d, channel_index=0)

    notes: List[str] = []
    miss_ratio = _missing_ratio(ecg_raw)

    if miss_ratio > 0.05:
        notes.append(f"High missing_ratio={miss_ratio:.3f} (auto-interpolation applied).")

    if ecg_raw.size < MIN_SAMPLES_FOR_PROCESS:
        notes.append(f"Too short segment: n_samples={ecg_raw.size}.")
        return (
            _QualityReport(False, miss_ratio, 0.0, notes),
            RPeaksInfo(indices=[], method="neurokit2"),
            HrvTimeInfo(),
            np.asarray([], dtype=float),
        )

    ecg_cleaned = _clean_ecg(ecg_raw, segment.sampling_rate_hz)

    # Quality (optional)
    q_mean = 0.0
    try:
        q = _compute_quality(ecg_cleaned, segment.sampling_rate_hz)
        q_mean = float(np.nanmean(q)) if q.size else 0.0
    except Exception as exc:
        notes.append(f"ecg_quality failed: {exc}")
        q_mean = 0.0

    # R-peaks (required for HR/HRV)
    try:
        peaks = _detect_rpeaks(ecg_cleaned, segment.sampling_rate_hz)
    except Exception as exc:
        notes.append(f"R-peak detection failed: {exc}")
        return (
            _QualityReport(False, miss_ratio, q_mean, notes),
            RPeaksInfo(indices=[], method="neurokit2"),
            HrvTimeInfo(),
            np.asarray([], dtype=float),
        )

    rr_ms = _rr_intervals_ms(peaks, segment.sampling_rate_hz)

    # HRV time
    if peaks.size < MIN_RPEAKS_FOR_HRV:
        notes.append(f"Not enough R-peaks for HRV: n_peaks={int(peaks.size)}.")
        signal_ok = False
        hrv = HrvTimeInfo()
    else:
        # Prefer RR-based stable calculation for summary usage
        hrv = _hrv_from_rr(rr_ms)
        signal_ok = True

    return (
        _QualityReport(signal_ok, miss_ratio, round(q_mean, 4), notes if notes else ["ok"]),
        RPeaksInfo(indices=peaks.tolist(), method="neurokit2"),
        hrv,
        rr_ms,
    )


@app.get("/health")
<<<<<<< HEAD
def health() -> Dict[str, bool]:
    return {"ok": True}


@app.post("/ecg/features", response_model=EcgFeatures)
def ecg_features(segment: EcgSegment) -> EcgFeatures:
    q, rpeaks, hrv, _ = _process_segment(segment)
    return EcgFeatures(
        segment_id=segment.segment_id,
        quality=QualityInfo(
            signal_ok=q.signal_ok,
            missing_ratio=round(q.missing_ratio, 6),
            quality_index_mean=round(q.quality_index_mean, 4),
            notes=q.notes,
        ),
        rpeaks=rpeaks,
        hrv_time=hrv,
    )


@app.post("/ecg/pomodoro/end", response_model=PomodoroWorkSummary)
def end_pomodoro(req: PomodoroWorkRequest) -> PomodoroWorkSummary:
    # Ensure chronological order for trend & RR concatenation
    segments = sorted(req.segments, key=lambda s: s.start_time_unix_ms)

    rr_all: List[float] = []
    q_means: List[float] = []
    miss_ratios: List[float] = []
    signal_ok_count = 0
    notes: List[str] = []
    trend: List[TrendPoint] = []

    for seg in segments:
        q, _, hrv, rr_ms = _process_segment(seg)

        rr_all.extend(rr_ms.tolist())
        q_means.append(float(q.quality_index_mean))
        miss_ratios.append(float(q.missing_ratio))
        signal_ok_count += int(q.signal_ok)
        notes.extend(q.notes)

        t_offset_s = int(max(0, (seg.start_time_unix_ms - req.work_start_unix_ms) // 1000))
        trend.append(
            TrendPoint(
                t_offset_s=t_offset_s,
                mean_hr_bpm=hrv.mean_hr_bpm,
                rmssd_ms=hrv.rmssd_ms,
                sdnn_ms=hrv.sdnn_ms,
                quality_index_mean=float(q.quality_index_mean),
                signal_ok=q.signal_ok,
            )
        )

    rr_all_arr = np.asarray(rr_all, dtype=float)

    hrv_total = _hrv_from_rr(rr_all_arr)
    rr_sum = _rr_summary(rr_all_arr)

    # HR summary derived from RR distribution (per-beat HR)
    if rr_all_arr.size > 0:
        hr_inst = 60000.0 / rr_all_arr
        hr_sum = HrSummary(
            mean_bpm=round(float(np.mean(hr_inst)), 2),
            min_bpm=round(float(np.min(hr_inst)), 2),
            max_bpm=round(float(np.max(hr_inst)), 2),
        )
    else:
        hr_sum = HrSummary()

    # Aggregate quality
    n_seg = max(1, len(segments))
    q_mean_total = float(np.mean(q_means)) if q_means else 0.0
    miss_mean_total = float(np.mean(miss_ratios)) if miss_ratios else 1.0
    signal_ok_ratio = signal_ok_count / float(n_seg)

    # Define overall signal_ok conservatively
    overall_ok = bool(signal_ok_ratio >= 0.7 and rr_all_arr.size >= 10)

    # De-duplicate notes (keep order)
    seen = set()
    uniq_notes = []
    for n in notes:
        if n not in seen:
            uniq_notes.append(n)
            seen.add(n)

    return PomodoroWorkSummary(
        user_id=req.user_id,
        session_id=req.session_id,
        work_start_unix_ms=req.work_start_unix_ms,
        work_end_unix_ms=req.work_end_unix_ms,
        duration_s=int(max(0, (req.work_end_unix_ms - req.work_start_unix_ms) // 1000)),
        quality=QualityInfo(
            signal_ok=overall_ok,
            missing_ratio=round(miss_mean_total, 6),
            quality_index_mean=round(q_mean_total, 4),
            notes=uniq_notes if uniq_notes else ["ok"],
        ),
        hr_summary=hr_sum,
        hrv_time=hrv_total,
        rr_summary=rr_sum,
        trend_1min=trend,
=======
def health():
    return {"status": "ok", "processing": processing_active}

@app.post("/ecg/pomodoro/end", response_model=PomodoroSummary)
def end_pomodoro(session_id: str, duration_min: int = 25):
    """Triggered when pomodoro ends to generate summary."""
    fs = 360
    # Simulate data for a representative 30-second segment
    raw, fs = get_mit_bih_data(sampto=fs * 30) 
    res = process_ecg(raw, fs)
    plot_path = generate_vis(res, fs, f"summary_{session_id}.png")
    
    summary = PomodoroSummary(
        session_id=session_id,
        start_time=int(time.time() - duration_min * 60),
        end_time=int(time.time()),
        avg_hr=round(res['hr_bpm'], 2),
        avg_sdnn=round(res['sdnn_ms'], 2),
        stress_percentage=30.0, # Placeholder
        total_samples=len(raw),
        plot_url=plot_path
    )
    
    with open(SUMMARY_FILE, "w") as f:
        json.dump(summary.dict(), f)
        
    return summary

@app.post("/ecg/features", response_model=EcgFeatures)
def ecg_features(segment: EcgSegment) -> EcgFeatures:
    """Manual feature extraction endpoint."""
    fs = segment.sampling_rate_hz
    # Flatten samples if provided as [[s1], [s2]]
    raw = np.array(segment.samples).flatten()
    res = process_ecg(raw, fs)
    
    # Calculate wave durations in ms
    p_wave_ms = (res['p_waves'][0][1] - res['p_waves'][0][0]) / fs * 1000 if res['p_waves'] else 0
    t_wave_ms = (res['t_waves'][0][1] - res['t_waves'][0][0]) / fs * 1000 if res['t_waves'] else 0
    qrs_ms = (res['qrs'][0][1] - res['qrs'][0][0]) / fs * 1000 if res['qrs'] else 0
    
    return EcgFeatures(
        segment_id=segment.segment_id,
        p_wave_ms=round(p_wave_ms, 2),
        t_wave_ms=round(t_wave_ms, 2),
        qrs_complex_ms=round(qrs_ms, 2),
        rr_intervals_ms=[round(x, 2) for x in res['rr_ms']],
        hrv_sdnn_ms=round(res['sdnn_ms'], 2),
        hr_bpm=round(res['hr_bpm'], 2),
        quality={"signal_ok": True}
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9
    )
