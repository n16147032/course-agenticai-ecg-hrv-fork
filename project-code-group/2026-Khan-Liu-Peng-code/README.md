# 🫀 HRV Coach Pro v2.1

An autonomous agentic AI system that processes ECG signals and produces clinician-grade Heart Rate Variability (HRV) reports with one click.

## 🎯 Overview

The **HRV Coach Pro v2.1** is an intelligent pipeline that:
- **Automatically** selects optimal preprocessing strategies
- **Iteratively** tries different R-peak detection methods
- **Validates** signal quality and retries with alternative approaches
- **Generates** comprehensive HRV reports with visualizations

## ✨ Features

### 🤖 **NEW: AI-Powered Mode (OpenRouter)**
- **DeepSeek V3.2 Integration**: Uses high-performance OpenRouter models for clinical insight.
- **Intelligent Reasoning**: Analyzes signal characteristics and explains them in plain English.
- **Professional PDF Reports**: Aesthetic, downloadable reports tailored for clients.
- **Adaptive Learning**: Learns from signal noise and adjusts strategy dynamically (Strategies A-D).

### 📊 Rule-Based Mode (Classic)
- **Agentic Decision-Making**: Sense → Decide → Act → Verify → Retry loop
- **Multiple Strategies**: A (Standard), B (Strong), C (Minimal), **D (Aggressive 5-20Hz)**.
- **Fail-Safe Robustness**: Accepts Grades A-E to ensure report generation even on noisy local data.
- **Visual Reports**: ECG plots, R-peak overlays, RR tachograms.
- **Audit Trail**: Complete decision log in JSON format.

## 🚀 Quick Start

### Installation

```bash
cd hrv_coach_agent
pip install -r requirements.txt
```

### Setup OpenRouter API (Optional - for AI mode)

1. Get your API key from [OpenRouter](https://openrouter.ai/)
2. Create a `.env` file:
```bash
cp .env.example .env
```
3. Edit `.env` and add your key:
```
OPENROUTER_API_KEY=your_key_here
```

### CLI Usage

**Rule-Based Mode (No API needed):**
```bash
python -m hrv_agent.run --record 100 --dataset mitdb --out outputs/run_001
```

**🤖 AI Mode:**
```bash
python -m hrv_agent.run --record 100 --dataset mitdb --use-openrouter
```

### Streamlit UI

```bash
python -m streamlit run app.py
```

Then open your browser to `http://localhost:8501`

- Toggle between **Rule-Based** and **OpenRouter AI** modes.
- Drag & Drop local CSV files or select PhysioNet records.
- **Download PDF Report** directly from the sidebar.

## 📊 Output

### Rule-Based Mode
- `report.md` - Technical markdown report.
- `plots.png` - Visualizations (ECG, R-peaks, tachogram).
- `agent_log.json` - Complete audit trail.

### AI Mode
- `gemini_report.md` - **AI-generated clinical report**.
- `report.pdf` - **Professional PDF Report**.
- `plots.png` - Visualizations.

## 🏗️ Architecture

### Agentic Policy Loop

1. **Sense**: Load ECG data (PhysioNet or Local CSV).
2. **Decide**: Select preprocessing strategy (A/B/C/D).
3. **Act**: Apply filtering and detect R-peaks.
4. **Verify**: Validate signal quality (A-E Grading).
5. **Retry**: If quality is poor (Grade < E), try alternative strategies.

### Strategies

| Strategy | Preprocessing | Use Case |
|----------|---------------|----------|
| A | Standard (0.5-40Hz) | Clean clinical signals |
| B | Strong Filter (Biosppy) | Moderate noise |
| C | Minimal (Highpass only) | Very high quality recordings |
| **D** | **Aggressive (5-20Hz)** | **Messy/Local 50Hz data** |

## 📁 Project Structure

```
hrv_coach_agent/
├── hrv_agent/
│   ├── __init__.py
│   ├── agent.py          # Rule-based agent
│   ├── openrouter_agent.py # 🤖 NEW: OpenRouter/DeepSeek agent
│   ├── config.py         # API configuration
│   ├── prompts.py        # System prompts
│   ├── pdf_generator.py  # 📄 NEW: PDF engine
│   ├── data.py           # Smart Loader (WFDB + CSV)
│   ├── tools.py          # DSP (Strategies A-D)
│   ├── metrics.py        # HRV calculations
│   ├── run.py            # CLI entry point
│   ├── plotting.py
│   └── report.py
├── tests/
│   └── test_basic.py     # Unit tests
├── app.py                # Streamlit UI
├── requirements.txt
└── README.md
```

## ⚠️ Limitations

- **Not for clinical diagnosis** - Educational/research purposes only.
- Requires internet for OpenRouter AI features.
- Local data must be single-channel ECG (or CSV with timestamps).

## 📄 License

Educational use only. Dataset usage follows PhysioNet terms.
