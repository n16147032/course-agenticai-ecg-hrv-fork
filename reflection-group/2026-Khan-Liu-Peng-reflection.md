# Group Reflection — HRV Coach Pro v2.1

**Group:** [Admin / Team Name]  
**Year:** 2026  

---

## 1. What Worked Well

- **Hybrid Intelligence**: The combination of **OpenRouter/DeepSeek** for high-level reasoning and a robust Rule-Based engine for fail-safe operations proved ideal. The transition to OpenRouter provided reliable access to high-performance models (DeepSeek V3.2) without the quota instability of the previous Gemini implementation.
- **Fail-Safe Robustness**: The new "Grade E" acceptance policy and **Strategy D** (Aggressive Filtering) allowed the system to generate valid reports even for extremely noisy local data that would have crashed a standard pipeline.
- **Professional Deliverables**: Pivoting to PDF exports via `reportlab` significantly elevated the perceived value of the tool, offering a tangible "product" rather than just a dashboard view.

---

## 2. Challenges & Lessons Learned

- **The "Local Data" Reality Check**: We initially assumed 50Hz local data would be similar to clinical MITDB records. In reality, it was plagued by noise and indeterminate sampling rates. This forced us to engineer a **smart CSV loader** and "Strategy D" (5-20Hz filtering) to ignore muscle artifacts.
- **API Model Volatility**: Relying on a single provider (Gemini) caused interruptions when quotas were hit or models deprecated. Switching to an aggregator like **OpenRouter** gave us model stability and flexibility.
- **NumPy 2.x Compatibility**: Managing the transition to Python 3.14/NumPy 2.x required monkeypatching legacy libraries (`neurokit2`), teaching us the importance of dependency management in evolving ecosystems.

---

## 3. What We Would Improve Next

- **Interactive Correction**: Allowing the user to manually "mark" valid R-peaks on the plot to retrain the detector in real-time.
- **Real-Time Streaming**: Adapting the pipeline to process live Bluetooth streams from wearable sensors.
- **Fully Local AI**: Experimenting with quantized local models (like DeepSeek-Coder-1.3B) to remove the internet dependency entirely.

---

## 4. Conclusion

This project successfully demonstrated that **Agentic AI** isn't just about chat—it's about adding a resilient decision-making layer to signal processing. By autonomously adapting to noise and pivoting strategies, the agent turns "bad data" into "usable insights."
