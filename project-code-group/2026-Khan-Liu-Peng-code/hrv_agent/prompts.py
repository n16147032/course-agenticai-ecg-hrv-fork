"""System prompts and templates for Gemini-powered HRV analysis"""

SYSTEM_PROMPT = """You are a professional HRV analyst. Provide clear, structured insights using bullet points and summaries. Keep responses under 200 words. Focus on practical health insights and actionable recommendations."""

STRATEGY_SELECTION_PROMPT = """Analyze signal stats and recommend strategy.

Stats:
- fs: {fs} Hz
- span: {duration}s
- amp: {mean_amp} ± {std_amp}
- drift: {baseline_wander}

Choices:
A (Standard), B (Strong Filter), C (Minimal)
Detectors: neurokit, pantompkins

Return:
STRATEGY: [A/B/C]
DETECTOR: [method]
REASON: [1-sentence reasoning]"""

QUALITY_INTERPRETATION_PROMPT = """Analyze quality.
Grade: {grade} | HR: {mean_hr} | Irregularity: {outlier_ratio}
Detail: {reason}

Return:
1. Reliability (High/Med/Low)
2. Verdict (Valid/Invalid)
3. Action"""

CLINICAL_REPORT_PROMPT = """Analyze this HRV data and create a professional summary (MAX 200 WORDS):

**Data:**
- Record: {record_id} | Grade: {grade}
- SDNN: {sdnn}ms | RMSSD: {rmssd}ms | LF/HF: {lf_hf_ratio}

**Format Required:**

## Summary
[2-3 sentence overview of overall heart health and stress/recovery balance]

## Key Findings
- **Heart Rate Variability**: [Interpret SDNN - is it good/moderate/low?]
- **Recovery Capacity**: [Interpret RMSSD - vagal tone assessment]
- **Stress Balance**: [Interpret LF/HF ratio - sympathetic vs parasympathetic]

## Recommendation
[ONE specific, actionable suggestion to improve HRV]

**Rules:**
- Maximum 200 words TOTAL
- Use bullet points for Key Findings
- Be conversational and clear
- Focus on practical insights
- Include one actionable recommendation

Write the report now:"""

RETRY_DECISION_PROMPT = """Current: Grade {grade} | {strategy}/{detector} | {reason}
History: {history}

Decision: [Accept/Retry/Reject]
Next Strategy: [A/B/C or None]
Next Detector: [method or None]"""

