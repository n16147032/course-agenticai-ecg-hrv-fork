# HRV Coach Pro v2.1 — Technical Report

**Student:** Saquib Khan
**Year:** 2026  

---

## 1. System Overview

This project implements a hybrid agentic pipeline that transforms raw ECG signals into clinical HRV insights. The system is "agentic" in its ability to autonomously sense signal quality, decide on optimal processing strategies, and iteratively retry processing steps to achieve a result even from noisy local data. 

A unique feature is the **dual-brain architecture**:
- **Rule-Based Engine**: Fast, deterministic, and always available offline.
- **OpenRouter AI Engine**: Uses **DeepSeek V3.2** via OpenRouter for high-precision clinical interpretation and actionable insights.

---

## 2. Data Source and Ethics

### 2.1 Dataset
The system utilizes:
- **PhysioNet Databases**: MIT-BIH Arrhythmia Database (mitdb) via `wfdb`.
- **Local CSV Data**: A robust ingestion pipeline for local 50Hz recordings with **smart sampling rate detection**.

### 2.2 Ethics / Privacy
- **Privacy by Design**: Raw ECG signals are processed locally; only anonymous summary metrics are sent to the AI API.
- **Disclaimer**: Every report includes a mandatory disclaimer stating results are for educational/demo purposes and not for medical diagnosis.

---

## 3. Pipeline and Agent Design

### 3.1 The Agentic Loop
The agent follows a **Sense-Decide-Act-Verify-Retry** loop:
1. **Sense**: Load signal + compute noise/amplitude stats.
2. **Decide**: Select Strategy A (Standard), B (Strong Filter), C (Minimal), or **D (Aggressive)**.
3. **Act**: Preprocess ECG + Detect R-peaks.
4. **Verify**: Grade the output (Outlier ratio, HR range).
5. **Retry**: If Grade < E, loop back to Step 2 with the next candidate strategy.

### 3.2 Key Strategies
- **Strategy A**: 0.5Hz Highpass + 50/60Hz Notch (Standard).
- **Strategy B**: Robust Bandpass (0.67-45Hz).
- **Strategy C**: Minimalist Highpass (0.5Hz).
- **Strategy D (New)**: **Aggressive QRS Enhancement** (5-20Hz Bandpass). Specifically designed for 50Hz local data.

### 3.3 LLM Integration (DeepSeek V3.2)
The agent leverages OpenRouter to access DeepSeek V3.2 for:
- **Concise Clinical Reports**: Converting metrics like SDNN/RMSSD into 200-word, action-oriented summaries.
- **Cost Efficiency**: Optimized prompt engineering ensures high-value output with minimal tokens.

---

## 4. Engineering Solutions

### 4.1 Robust Local Data Loading
Local CSV files often suffer from unknown sampling rates or missing headers. I implemented a **smart loader** that:
- Auto-detects column indices for ECG/PPG.
- Infers specific sampling rates from timestamp deltas to prevent heart rate calculation errors.

### 4.2 Professional PDF Export
To provide a complete product experience, I integrated `reportlab` to generate **professional PDF reports** featuring:
- Clinical summaries with proper typography.
- Color-coded signal quality indicators.
- Embedded signal visualizations (restricted to 10s for clarity).

### 4.3 Fail-Safe Grading
To prevent "Analysis Failed" errors on consumer-grade hardware/data, the validator now accepts grades **A through E**, ensuring a report is always generated while transparently flagging signal quality issues.

---

## 5. Results

### 5.1 Success on Clean Signal (Record 100)
- **Grade**: A
- **SDNN**: 51.4ms (Healthy variability)
- **RMSSD**: 66.5ms
- **Result**: AI verified "Excellent autonomic balance".

### 5.2 Recovery on Noisy Local Data
Using **Strategy D**, the agent successfully locked onto R-peaks in a noisy 50Hz local recording that failed standard processing, achieving a Grade C result and providing valid HRV metrics.

---

## 6. Future Improvements

- **Auto-Windowing**: Implement an agent that "scans" a 24-hour recording to find the cleanest 5-minute window for analysis.
- **Detector Consensus**: Running multiple detectors in parallel and using an agent to vote on the most likely R-peak locations.

---

## 7. How to Run

### Installation
```bash
pip install -r requirements.txt
```

### CLI Analysis
```bash
python -m hrv_agent.run --record 100 --use-openrouter
```

### Dashboard
```bash
streamlit run app.py
```
