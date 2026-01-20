# Group Tests — HRV Coach Pro v2.1

**Group:** 2026-Khan-Liu-Peng 
**Year:** 2026  

---

## 1. How to Run Tests

Ensure all dependencies are installed, then run the test suite from the root directory:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_basic.py -v
```

---

## 2. Test Coverage Summary

### 2.1 ECG Processing Tests
- **`test_preprocess_shape`**: Verifies that the preprocessing filters maintain the signal length and do not introduce NaNs or Inf values.
- **`test_preprocess_strategies`**: Confirms that Strategy A, B, and C can all be executed without crashing, ensuring the toolbox is robust.

### 2.2 R-Peak Detection Tests
- **`test_peak_detection`**: Uses a simulated 10-second ECG signal (10Hz sinus + noise) to verify that the R-peak detector finds a physiological number of beats (approx 10 beats for 60bpm).

---

## 3. Agentic Policy Checks (Manual/Integration)

### 3.1 Hybrid Decision Logic
The agent was tested with the `--use-openrouter` flag to verify:
1. **API Initialization**: Successful connection to Gemini-1.5-Flash.
2. **Strategy Loop**: Agent correctly attempts Strategy A → B → C if quality is low.
3. **Monkeypatch Verification**: Confirmed that HRV metrics compute correctly on NumPy 2.x environments by verifying `lf_power` is not None.

### 3.2 Graceful Degradation
- **Test Case**: API Key removed or Quota exceeded.
- **Expected Result**: System displays a `[!NOTE]` warning and provides a summarized rule-based clinical report instead of crashing.
- **Status**: ✅ **PASSED**

---

## 4. Acceptance Criteria

| Feature | Requirement | Status |
|---------|-------------|--------|
| One-Click UI | Start analysis with a single button | ✅ Pass |
| Autonomous Retry | Agent changes strategy on poor quality | ✅ Pass |
| Metrics Accuracy | SDNN/RMSSD within expected ranges | ✅ Pass |
| AI Interpretation | Condensed clinical summary generated | ✅ Pass |
| Fallback | Working report without API access | ✅ Pass |
