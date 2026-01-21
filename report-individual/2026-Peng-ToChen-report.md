# Technical Report: HRV Coach Pro v2.1 — Hybrid Agentic Pipeline for Robust ECG Analysis

**Author:** 2026-ToChen-Peng
**Group Members:** Khan Saquib, Liu Tzuen Andrew, ToChen Peng
**License:** CC-BY-4.0

## Abstract

This report details the development of *HRV Coach Pro v2.1*, an autonomous agentic system designed to transform raw ECG signals into clinical-grade Heart Rate Variability (HRV) insights. Addressing the challenges of signal noise and interpretation, the system implements a "Dual-Brain" architecture combining a deterministic rule-based engine with the DeepSeek V3.2 Large Language Model (LLM) via OpenRouter. The core workflow operates on a closed-loop "Sense-Decide-Act-Verify" cycle, allowing the agent to autonomously grade signal quality and iteratively retry processing with adaptive filtering strategies (including a novel Strategy D for noisy 50Hz data). Results demonstrate that the system can recover usable metrics from noisy local recordings where standard algorithms fail, providing both professional PDF exports and transparent audit trails.

## Introduction

Heart Rate Variability (HRV) is a critical biomarker for assessing autonomic nervous system regulation, useful in healthcare and stress monitoring. However, analyzing HRV from raw ECG data is fraught with challenges, including baseline drift, motion artifacts, and varying sampling rates in local CSV files.

Traditional workflows rely heavily on manual inspection or static algorithms that fail when noise is present ("Analysis Failed"). Furthermore, while chat-based AI tools can offer interpretation, they lack the ability to execute end-to-end signal processing or validate their own outputs.

Our objective was to build an agentic AI that acts as a closed-loop system. It does not merely process data but "senses" quality, "decides" on strategies, and "verifies" results against physiological constraints to ensure robust, actionable output without human intervention.

## System Architecture

The system utilizes a modular agent architecture driven by an autonomous orchestrator.

### 4-Stage Agentic Loop
The core logic follows a **Sense-Decide-Act-Verify** workflow:

1.  **Sense:** The agent ingests the ECG signal and computes statistics (noise levels, amplitude stats, sampling rate).
2.  **Decide:** Based on the sensed data, it selects a processing strategy (A, B, C, or D).
3.  **Act:** The system executes preprocessing, R-peak detection, and HRV metric calculation.
4.  **Verify & Retry:** The output is graded (A through E). If the grade is insufficient (e.g., physiological outliers detected), the agent loops back to Step 2 to select a different strategy.

### Dual-Brain Architecture
To balance cost, speed, and intelligence, the system employs two "brains":
* **Rule-Based Engine:** Handles fast, deterministic signal processing and basic grading. Available offline.
* **AI Engine (DeepSeek V3.2):** Accessed via OpenRouter, this engine generates high-precision clinical interpretations and 200-word action-oriented summaries, optimizing for token cost efficiency.

## Implementation

### 1. Robust Data Ingestion
We implemented a **smart loader** capable of handling MIT-BIH databases (via `wfdb`) and local CSV files. The loader auto-detects column indices and infers sampling rates from timestamp deltas to prevent heart rate calculation errors.

### 2. Adaptive Processing Strategies
The agent switches between four distinct strategies based on the "Verify" stage feedback:
* **Strategy A:** Standard processing (0.5Hz Highpass + Notch).
* **Strategy B:** Robust Bandpass (0.67-45Hz).
* **Strategy C:** Minimalist Highpass (0.5Hz).
* **Strategy D (Aggressive):** Specifically engineered for noisy 50Hz local data, utilizing a 5-20Hz Bandpass filter for aggressive QRS enhancement.

### 3. Validation and Grading
Instead of a binary Pass/Fail, we implemented a graded validator (A/B/C/Reject). This ensures a report is generated whenever possible while transparently flagging signal quality. Validation checks include heart rate range plausibility and RR interval outlier ratios.

### 4. Professional Reporting
The `reportlab` library was integrated to generate professional PDF reports. These include color-coded quality indicators, 10-second signal visualizations, and the AI-generated clinical summary, complete with a mandatory medical disclaimer.

## Results

### Performance on Clean Data
When tested on clean records (e.g., MIT-BIH Record 100):
* **Grade:** A
* **Metrics:** SDNN 51.4ms, RMSSD 66.5ms.
* **Outcome:** The AI verified the metrics as "Excellent autonomic balance".

### Robustness on Noisy Data
The system's adaptability was tested on noisy local recordings. Initial standard strategies failed, but the agent's retry logic triggered **Strategy D**. This successfully locked onto R-peaks, achieving a **Grade C** result and providing valid HRV metrics instead of an error.

### Auditability
Every analysis produces a structured audit log documenting the agent's decision path (e.g., "Strategy A failed, retrying with Strategy B"), ensuring traceability.

## Discussion

### Challenges
A significant challenge was balancing the strictness of the validator. If too strict, the system rejects usable data; if too loose, it produces artifacts. The "Graded" approach (A-E) proved to be a practical solution. Additionally, processing local CSVs required handling unknown headers and varying sampling rates, which the smart loader successfully addressed.

### Limitations
* **Baseline:** The system currently interprets data based on general population norms, lacking subject-specific personalization.
* **Metrics:** Analysis is currently limited to time-domain metrics (SDNN, RMSSD).

### Lessons Learned
The primary insight is that **workflow orchestration** is as critical as the algorithms themselves. The ability to "retry" allows the system to function in real-world scenarios where data is rarely perfect. Privacy-by-design (processing signals locally) also proved feasible without sacrificing the quality of AI interpretation.

## Conclusion

HRV Coach Pro v2.1 demonstrates the power of Agentic AI in physiological signal analysis. By implementing a self-correcting **Sense-Decide-Act-Verify** loop and a **Dual-Brain** architecture, the system achieves robustness superior to traditional single-pass tools. Future work will focus on "Auto-Windowing" to scan 24-hour recordings for the best analysis windows and implementing detector consensus mechanisms.

## References

1. Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. (1996). Heart rate variability: standards of measurement, physiological interpretation and clinical use. *Circulation*, 93(5), 1043–1065.
2. Pan, J., & Tompkins, W. J. (1985). A real-time QRS detection algorithm. *IEEE Transactions on Biomedical Engineering*, 32(3), 230–236.