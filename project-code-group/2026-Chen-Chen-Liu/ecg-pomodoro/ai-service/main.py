from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from dotenv import load_dotenv

from models import EcgFeatures, PomodoroWorkSummary, AiPrediction, AiAdvice
=======
import google.generativeai as genai
import os
from dotenv import load_dotenv
from models import EcgFeatures, AiPrediction
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9

APP_ORIGINS = ["http://localhost:3000"]

app = FastAPI(title="AI Service", version="1.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=APP_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Optional Gemini
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = None
if GEMINI_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        MODEL = genai.GenerativeModel("gemini-2.5-flash-lite")
    except Exception:
        MODEL = None

=======
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    MODEL = genai.GenerativeModel("gemini-2.0-flash")
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9

@app.get("/health")
def health() -> dict:
    return {"ok": True, "gemini_enabled": MODEL is not None}


def _safe_float(x: Any, default: float = 0.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def _rule_predict_from_mean_hr(signal_ok: bool, mean_hr_bpm: float) -> Dict[str, Any]:
    if not signal_ok:
        return {
            "label": "unknown",
            "probabilities": {"focus": 0.0, "stress": 0.0, "neutral": 0.0, "unknown": 1.0},
            "explain": {"reason": "signal_not_ok"},
        }

    if mean_hr_bpm >= 90.0:
        return {
            "label": "stress",
            "probabilities": {"focus": 0.2, "stress": 0.8, "neutral": 0.0, "unknown": 0.0},
            "explain": {"rule": "mean_hr>=90"},
        }
    if mean_hr_bpm >= 75.0:
        return {
            "label": "neutral",
            "probabilities": {"focus": 0.55, "stress": 0.45, "neutral": 0.0, "unknown": 0.0},
            "explain": {"rule": "75<=mean_hr<90"},
        }
    return {
        "label": "focus",
        "probabilities": {"focus": 0.8, "stress": 0.2, "neutral": 0.0, "unknown": 0.0},
        "explain": {"rule": "mean_hr<75"},
    }


def _llm_json(prompt: str) -> Optional[Dict[str, Any]]:
    if MODEL is None:
        return None
    try:
        resp = MODEL.generate_content(prompt)
        text = getattr(resp, "text", "") or ""
        return json.loads(text)
    except Exception:
        return None


@app.post("/ai/predict", response_model=AiPrediction)
def predict(features: EcgFeatures) -> AiPrediction:
<<<<<<< HEAD
    signal_ok = bool(getattr(features.quality, "signal_ok", False))
    mean_hr = _safe_float(getattr(features.hrv_time, "mean_hr_bpm", 0.0))

    rule = _rule_predict_from_mean_hr(signal_ok, mean_hr)
    return AiPrediction(
        segment_id=features.segment_id,
        model={"name": "rule_mvp", "version": "1.1.0"},
        label=rule["label"],
        probabilities=rule["probabilities"],
        explain={"used": ["quality.signal_ok", "hrv_time.mean_hr_bpm"], "mean_hr_bpm": mean_hr, **rule["explain"]},
    )


@app.post("/ai/advice", response_model=AiAdvice)
def advice(features: EcgFeatures) -> AiAdvice:
    pred = predict(features)
    mean_hr = _safe_float(getattr(features.hrv_time, "mean_hr_bpm", 0.0))
    signal_ok = bool(getattr(features.quality, "signal_ok", False))

    if not signal_ok:
        return AiAdvice(
            segment_id=features.segment_id,
            title="訊號品質不足",
            bullets=["請確認感測器貼合位置與接觸品質。", "保持靜止 10–20 秒後再重試。"],
            safety_note="此建議僅供專題展示，不可用於醫療判斷。",
            used_metrics={"signal_ok": signal_ok, "mean_hr_bpm": mean_hr},
        )

    if pred.label == "stress":
        title = "建議：降壓休息"
        bullets = [
            "做 4-6 呼吸：吸氣 4 秒、吐氣 6 秒，重複 5 次。",
            "肩頸伸展 30 秒，視線看遠方放鬆。",
            "下一輪工作先從最小任務開始（例如 5 分鐘）。",
        ]
    elif pred.label == "neutral":
        title = "建議：輕量休息"
        bullets = ["起身喝水、走動 1 分鐘。", "檢查下一輪待辦：只留 1 個最重要任務。"]
    else:
        title = "建議：保持節奏"
        bullets = ["喝水、遠眺 20 秒，避免久坐疲勞。", "下一輪延續同一個任務，降低切換成本。"]

    return AiAdvice(
        segment_id=features.segment_id,
        title=title,
        bullets=bullets,
        safety_note="此建議僅供專題展示，不可用於醫療判斷。",
        used_metrics={"signal_ok": signal_ok, "mean_hr_bpm": mean_hr, "label": pred.label},
    )

import re

def _dump_model(x: Any) -> Dict[str, Any]:
    # pydantic v2: model_dump(); v1: dict()
    if hasattr(x, "model_dump"):
        return x.model_dump()
    if hasattr(x, "dict"):
        return x.dict()
    return dict(x)

def _try_parse_json(text: str) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(text)
    except Exception:
        pass
    # 嘗試從回覆中抓第一段 {...}
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

def _llm_call(prompt: str) -> Dict[str, Any]:
    resp = MODEL.generate_content(prompt)  # 這行就是「真的打到 LLM」[web:51]
    text = getattr(resp, "text", "") or ""
    parsed = _try_parse_json(text)
    return {"raw_text": text, "parsed": parsed}

@app.post("/ai/pomodoro/advice", response_model=AiAdvice)
def pomodoro_advice(summary: PomodoroWorkSummary) -> AiAdvice:
    seg_id = summary.session_id
    signal_ok = bool(summary.quality.signal_ok)
    mean_hr = _safe_float(summary.hrv_time.mean_hr_bpm)
    sdnn = _safe_float(summary.hrv_time.sdnn_ms)
    rmssd = _safe_float(summary.hrv_time.rmssd_ms)
    outlier_ratio = _safe_float(summary.rr_summary.outlier_ratio)

    # 只要模型可用且訊號OK：一定呼叫 LLM
    if MODEL is not None and signal_ok:
        payload = _dump_model(summary)
        prompt = f"""
你是一個番茄鐘休息建議助手。請根據「ECG 摘要 JSON」產生休息建議。
請嚴格遵守：

規則：
1) 只輸出「單一 JSON 物件」，不要 markdown、不要多餘文字。
2) bullets 限制 3–4 點，每點 12–25 字，務必可執行（呼吸/伸展/喝水/走動/下一輪策略）。
3) 必須在 used_metrics 填入你「實際參考」的數值，且至少包含 mean_hr_bpm、rmssd_ms、sdnn_ms、rr_outlier_ratio 中的 2 個。
4) 若 rmssd_ms 或 sdnn_ms 為 0（或 rr_summary.n 很小），請在 bullets 提醒「本次 HRV 可信度有限」。

ECG 摘要 JSON：
{json.dumps(payload, ensure_ascii=False)}

輸出 JSON 格式（照抄 key，不要加 key）：
{{
  "title": "一句話總結（<=12字）",
  "bullets": ["...", "...", "..."],
  "safety_note": "此建議僅供專題展示，不可用於醫療判斷。",
  "used_metrics": {{
    "mean_hr_bpm": 0,
    "sdnn_ms": 0,
    "rmssd_ms": 0,
    "rr_outlier_ratio": 0
  }}
}}

範例輸出（僅示意格式，數值請依摘要填）：
{{
  "title": "建議：降壓休息",
  "bullets": [
    "做 4-6 呼吸 1 分鐘",
    "起身走動 1–2 分鐘",
    "補水後再開始下一輪",
  ],
  "safety_note": "此建議僅供專題展示，不可用於醫療判斷。",
  "used_metrics": {{
    "mean_hr_bpm": 92,
    "sdnn_ms": 28,
    "rmssd_ms": 18,
    "rr_outlier_ratio": 0.12
  }}
}}
"""

        r = _llm_call(prompt)
        raw = (r["raw_text"] or "").strip()
        parsed = r["parsed"]

        if isinstance(parsed, dict) and "title" in parsed and "bullets" in parsed:
            used_metrics = parsed.get("used_metrics") or {}
            used_metrics["used_llm"] = True
            return AiAdvice(
                segment_id=seg_id,
                title=str(parsed["title"]),
                bullets=[str(x) for x in (parsed.get("bullets") or [])][:4],
                safety_note=str(parsed.get("safety_note", "此建議僅供專題展示，不可用於醫療判斷。")),
                used_metrics=used_metrics,
            )

        return AiAdvice(
            segment_id=seg_id,
            title="LLM 回覆（raw preview）",
            bullets=[raw[:400] if raw else "(empty)"],
            safety_note="此建議僅供專題展示，不可用於醫療判斷。",
            used_metrics={"used_llm": True, "note": "json_parse_failed"},
        )

    # ---- rule-based fallback（完全不碰 LLM）----
    if not signal_ok:
        return AiAdvice(
            segment_id=seg_id,
            title="訊號品質不足（本次摘要不可靠）",
            bullets=["休息時請確認感測器貼合。", "下次工作段開始前保持靜止 10–20 秒再開始。"],
            safety_note="此建議僅供專題展示，不可用於醫療判斷。",
            used_metrics={"signal_ok": signal_ok, "used_llm": False},
        )

    if mean_hr >= 90.0 or (sdnn > 0 and sdnn < 50.0) or (outlier_ratio > 0.2):
        title = "建議：降壓＋降低刺激"
        bullets = [
            "做 4-6 呼吸 1 分鐘，讓心率回落。",
            "離開螢幕、走動 1–2 分鐘。",
            "下一輪先做低切換成本任務（整理/收尾）。",
        ]
    elif mean_hr >= 75.0:
        title = "建議：中等休息"
        bullets = ["補水＋伸展。", "快速確認下一輪目標，只保留 1 件最重要的事。"]
    else:
        title = "建議：維持節奏"
        bullets = ["補水、遠眺 20 秒。", "下一輪延續同一任務，避免頻繁切換。"]

    return AiAdvice(
        segment_id=seg_id,
        title=title,
        bullets=bullets,
        safety_note="此建議僅供專題展示，不可用於醫療判斷。",
        used_metrics={
            "mean_hr_bpm": mean_hr,
            "sdnn_ms": sdnn,
            "rmssd_ms": rmssd,
            "rr_outlier_ratio": outlier_ratio,
            "used_llm": False,
        },
    )
 
=======
    """
    Use Gemini to provide health suggestions based on ECG data.
    """
    # Extract relevant ECG metrics
    hrv_time = features.hrv_time or {}
    mean_hr = float(hrv_time.get("mean_hr_bpm", 0.0))
    rpeaks = features.rpeaks or {}
    quality = features.quality or {}
    
    # Build prompt for Gemini
    prompt = f"""
    Analyze the following ECG data and provide health suggestions:
    
    - Mean Heart Rate: {mean_hr} BPM
    - Rpeaks Data: {json.dumps(rpeaks, indent=2)}
    - Quality Score: {json.dumps(quality, indent=2)}
    
    Based on this data, provide:
    1. A classification: either "stress" or "focus" (stress if HR >= 90, focus otherwise)
    2. 2-3 practical health suggestions for the user
    3. Any concerning patterns to note
    
    Format your response as JSON with keys: classification, suggestions (list), concerns (list)
    """
    try:
        # Call Gemini API
        response = MODEL.generate_content(prompt)
        gemini_response = response.text
        
        # Parse the response (expecting JSON format)
        try:
            result = json.loads(gemini_response)
            label = result.get("classification", "focus")
            suggestions = result.get("suggestions", [])
            concerns = result.get("concerns", [])
        except json.JSONDecodeError:
            # Fallback if response isn't valid JSON
            label = "stress" if mean_hr >= 90.0 else "focus"
            suggestions = [gemini_response[:200]]
            concerns = []
        
        # Set probabilities based on classification
        probs = {"focus": 0.2, "stress": 0.8} if label == "stress" else {"focus": 0.8, "stress": 0.2}
        
        return AiPrediction(
            segment_id=features.segment_id,
            model={"name": "gemini-pro", "version": "1.0.0"},
            label=label,
            probabilities=probs,
            explain={
                "suggestions": suggestions,
                "concerns": concerns,
                "mean_hr_bpm": mean_hr,
            },
        )
    except Exception as e:
        # Fallback to simple rule-based if API fails
        if mean_hr >= 90.0:
            label = "stress"
            probs = {"focus": 0.2, "stress": 0.8}
        else:
            label = "focus"
            probs = {"focus": 0.8, "stress": 0.2}
        
        return AiPrediction(
            segment_id=features.segment_id,
            model={"name": "rule_fallback", "version": "0.0.1"},
            label=label,
            probabilities=probs,
            explain={"error": str(e), "used": ["hrv_time.mean_hr_bpm"]},
        )
>>>>>>> 7f0a1abcdb0603d56a817dad24a0d446c063c9e9
