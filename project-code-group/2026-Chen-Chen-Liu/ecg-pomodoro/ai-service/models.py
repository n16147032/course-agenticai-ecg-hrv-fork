from __future__ import annotations

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field


# ---- Shared-ish ECG contracts (LLM-friendly, no waveform) ----

class QualityInfo(BaseModel):
    signal_ok: bool
    missing_ratio: float = Field(ge=0.0, le=1.0)
    quality_index_mean: float = Field(ge=0.0, le=1.0)
    notes: List[str] = Field(default_factory=list)


class HrvTimeInfo(BaseModel):
    mean_hr_bpm: float = 0.0
    rmssd_ms: float = 0.0
    sdnn_ms: float = 0.0


class RPeaksInfo(BaseModel):
    method: str = "neurokit2"
    indices: List[int] = Field(default_factory=list)


class EcgFeatures(BaseModel):
    schema_version: Literal["ecg-feat/v1"] = "ecg-feat/v1"
    segment_id: str
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
    t_offset_s: int = Field(ge=0)
    mean_hr_bpm: float = 0.0
    rmssd_ms: float = 0.0
    sdnn_ms: float = 0.0
    quality_index_mean: float = 0.0
    signal_ok: bool = False


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


# ---- AI outputs ----

class AiPrediction(BaseModel):
    schema_version: Literal["ai-pred/v1"] = "ai-pred/v1"
    segment_id: str
    model: Dict = Field(default_factory=dict)
    label: str
    probabilities: Dict[str, float]
    explain: Optional[Dict] = None


class AiAdvice(BaseModel):
    schema_version: Literal["ai-advice/v1"] = "ai-advice/v1"
    segment_id: str
    title: str
    bullets: List[str]
    safety_note: str
    used_metrics: Dict
