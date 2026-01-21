# Technical Report: HRV Coach Pro v2.1 — An Agentic AI System for ECG-to-HRV Analysis  
  
**Author:** Liu Tzuen Andrew    
**Group Members:** Khan Squib  / ToChen Peng / Liu Tzuen Andrew   
**Course:** Agentic AI (ECG/HRV), NCKU Modular Program 2026    
  
**License:** CC-BY-4.0  
  
---  
  
## Abstract  
  
Heart rate variability (HRV) is a widely used biomarker for assessing autonomic nervous system activity, yet reliable extraction of HRV metrics from raw ECG data remains challenging due to signal noise, preprocessing sensitivity, and the need for expert interpretation. This report describes *HRV Coach Pro v2.1*, an agentic AI system that autonomously performs ECG preprocessing, R-peak detection, HRV computation, quality validation, and result interpretation. Unlike chat-based AI tools that generate single-pass responses, the proposed system operates as a closed-loop agent following a Sense–Decide–Act–Verify workflow, enabling adaptive strategy selection, retry, and graceful fallback. The system produces validated HRV metrics, interpretable reports, and a complete audit trail, demonstrating the practical advantages of agentic AI for robust physiological signal analysis.  
  
---  
  
## Introduction  
  
Heart rate variability (HRV) analysis plays an important role in healthcare, sports science, and stress monitoring by providing insights into autonomic nervous system regulation. However, transforming raw ECG recordings into reliable HRV metrics is not a trivial process. ECG signals are frequently affected by baseline drift, motion artifacts, and electrode noise, all of which can significantly impact R-peak detection and downstream HRV calculations.  
  
In many existing workflows, experts must manually inspect signals, adjust preprocessing parameters, and validate results. This manual process is time-consuming and difficult to scale, particularly for non-expert users. While chat-based AI systems can assist with analysis or interpretation, they typically lack the ability to autonomously validate results, retry failed strategies, or maintain a traceable decision history.  
  
The objective of this project was to design and implement an agentic AI system that can autonomously execute the full ECG-to-HRV pipeline, evaluate the quality of its own outputs, and adapt its workflow accordingly.  
  
---  
  
## System Architecture  
  
The proposed system follows a modular agent architecture centered on an autonomous orchestrator. The agent operates in a closed loop consisting of four stages: Sense, Decide, Act, and Verify.  
  
1. **Sense:** The agent extracts signal statistics from the raw ECG, such as noise level, signal span, and baseline drift.  
2. **Decide:** Based on sensed information, the agent selects a preprocessing strategy and R-peak detection method.  
3. **Act:** The chosen strategy is applied to filter the ECG, detect R-peaks, compute RR intervals, and calculate HRV metrics.  
4. **Verify:** The results are validated using physiological constraints (e.g., heart rate range, RR interval outliers). If quality is insufficient, the agent retries with an alternative strategy.  
  
This architecture allows the system to adapt dynamically to varying signal conditions rather than relying on a fixed, single-pass workflow.  
  
---  
  
## Implementation  
  
The system was implemented in Python using a combination of signal processing libraries and AI-assisted components.  
  
### Core Components  
  
- **ECG Loader:** Loads ECG data from PhysioNet via WFDB or from local files.  
- **Signal Processing Module:** Applies digital filtering and R-peak detection using established algorithms.  
- **HRV Metric Calculator:** Computes standard time-domain HRV metrics such as SDNN and RMSSD.  
- **Validator:** Checks physiological plausibility and assigns a quality grade (A/B/C/Reject).  
- **Orchestrator:** Coordinates all components, manages state, and controls retry and fallback logic.  
- **Report Generator:** Produces a concise, clinical-style Markdown report using either AI-assisted or rule-based interpretation.  
  
A key design choice was to ensure that all critical decisions—such as retrying preprocessing strategies—are made by the agent itself rather than being hard-coded or manually triggered.  
  
---  
  
## Results  
  
The system successfully performs end-to-end ECG-to-HRV analysis with no manual configuration. On clean ECG data, the agent consistently achieves high-quality (Grade A) results. When applied to noisy ECG signals, the agent autonomously retries alternative preprocessing strategies until acceptable quality is reached.  
  
Even in scenarios where the AI interpretation component is unavailable, the system remains functional by falling back to rule-based report generation. Each run produces not only HRV metrics and plots but also a structured audit log documenting all decisions made by the agent during execution.  
  
---  
  
## Discussion  
  
One of the main challenges encountered in this project was designing validation criteria that are strict enough to detect poor-quality results without being overly restrictive. Physiological constraints provided a practical balance between robustness and flexibility.  
  
A key lesson learned is that the primary value of agentic AI lies not in improving individual algorithms but in orchestrating them intelligently. The ability to verify outcomes and retry failed strategies significantly improves reliability compared to a single-pass, chat-based approach.  
  
Limitations of the current system include the absence of personalized HRV baselines and the focus on a limited set of HRV metrics. Future extensions could incorporate subject-specific calibration and additional frequency-domain or non-linear metrics.  
  
---  
  
## Conclusion  
  
This project demonstrates how an agentic AI architecture can enable robust and autonomous ECG-to-HRV analysis. By embedding validation, retry logic, and fallback mechanisms into the workflow, the system overcomes key limitations of traditional and chat-based approaches. The results highlight the importance of workflow design in agentic AI systems and suggest that similar architectures can be applied to other domains requiring reliable, interpretable, and self-verifying automation.  
  
---  
  
## References  
  
1. Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. (1996). Heart rate variability: standards of measurement, physiological interpretation and clinical use. *Circulation*, 93(5), 1043–1065.    
2. Pan, J., & Tompkins, W. J. (1985). A real-time QRS detection algorithm. *IEEE Transactions on Biomedical Engineering*, 32(3), 230–236.  
