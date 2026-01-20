"""
Data contract models for ECG processing service.

Stable, LLM-friendly:
- For LLM: only features/trends, no raw waveform in outputs.
- For ingestion: still accept EcgSegment with samples for computation.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Literal

from pydantic import BaseModel, Field


class Channel(BaseModel):
    """Channel metadata for a single signal channel."""
    name: str = Field(..., examples=["ECG"])
    unit: str = Field(..., examples=["adc"])
    lead: Optional[str] = Field(default=None, examples=["CH1"])


class EcgSegment(BaseModel):
    """Input payload: a short ECG segment in a unified format."""
    schema_version: Literal["ecg-seg/v1"] = "ecg-seg/v1"
    segment_id: str = Field(..., examples=["demo_1700000000000"])
    sampling_rate_hz: int = Field(..., ge=1, examples=[360])
    start_time_unix_ms: int = Field(..., examples=[1700000000000])
    channels: List[Channel]
    samples: List[List[float]] = Field(
        ...,
        description="2D array with shape [N, C]. Each row is one sample time.",
        examples=[[[0.12], [0.15], [0.10]]],
    )


<<<<<<< HEAD
class QualityInfo(BaseModel):
    signal_ok: bool = Field(..., description="True if features are reliable enough.")
    missing_ratio: float = Field(..., ge=0.0, le=1.0)
    quality_index_mean: float = Field(..., ge=0.0, le=1.0)
    notes: List[str] = Field(default_factory=list)


class RPeaksInfo(BaseModel):
    method: str = Field(default="neurokit2")
    indices: List[int] = Field(default_factory=list, description="Sample indices of R-peaks (segment-local).")


class HrvTimeInfo(BaseModel):
    mean_hr_bpm: float = 0.0
    rmssd_ms: float = 0.0
    sdnn_ms: float = 0.0

=======
class BioStatus(BaseModel):
    """Real-time biometric status."""
    timestamp_ms: int
    hr_bpm: float
    hrv_sdnn_ms: float
    signal_quality_score: float  # 0.0 to 1.0
    is_stressed: bool
    notes: Optional[str] = None

class UserBaseline(BaseModel):
    """User physiological baseline by time period."""
    user_id: str
    period_start_hour: int
    avg_hr: float
    avg_sdnn: float
    last_updated: int

class PomodoroSummary(BaseModel):
    """Summary of a completed Pomodoro session."""
    session_id: str
    start_time: int
    end_time: int
    avg_hr: float
    avg_sdnn: float
    stress_percentage: float
    total_samples: int
    plot_url: Optional[str] = None
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9

class EcgFeatures(BaseModel):
    """Output payload: extracted features from ECG segment."""
    schema_version: Literal["ecg-feat/v1"] = "ecg-feat/v1"
    segment_id: str
<<<<<<< HEAD
    quality: QualityInfo
    rpeaks: RPeaksInfo
    hrv_time: HrvTimeInfo


class RrSummary(BaseModel):
    n: int = 0
    mean_ms: float = 0.0
    std_ms: float = 0.0
    min_ms: float = 0.0
    max_ms: float = 0.0
    outlier_ratio: float = 0.0


class HrSummary(BaseModel):
    mean_bpm: float = 0.0
    min_bpm: float = 0.0
    max_bpm: float = 0.0


class TrendPoint(BaseModel):
    t_offset_s: int = Field(..., ge=0, description="Seconds from work_start_unix_ms.")
    mean_hr_bpm: float = 0.0
    rmssd_ms: float = 0.0
    sdnn_ms: float = 0.0
    quality_index_mean: float = 0.0
    signal_ok: bool = False


class PomodoroWorkRequest(BaseModel):
    schema_version: Literal["pomodoro-work/v1"] = "pomodoro-work/v1"
    user_id: str = Field(..., examples=["demo_user"])
    session_id: str = Field(..., examples=["pomodoro_001"])
    work_start_unix_ms: int = Field(..., examples=[1700000000000])
    work_end_unix_ms: int = Field(..., examples=[1700001500000])
    segments: List[EcgSegment] = Field(..., description="Recommend 1-minute segments in chronological order.")


class PomodoroWorkSummary(BaseModel):
    schema_version: Literal["pomodoro-summary/v1"] = "pomodoro-summary/v1"
    user_id: str
    session_id: str
    work_start_unix_ms: int
    work_end_unix_ms: int
    duration_s: int

    quality: QualityInfo
    hr_summary: HrSummary
    hrv_time: HrvTimeInfo
    rr_summary: RrSummary
    trend_1min: List[TrendPoint] = Field(default_factory=list)
=======
    p_wave_ms: float
    t_wave_ms: float
    qrs_complex_ms: float
    rr_intervals_ms: List[float]
    hrv_sdnn_ms: float
    hr_bpm: float
    quality: Dict
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9
