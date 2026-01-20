# Case Brief: Agentic ECG Analysis for Multi-Subject HRV Monitoring

**Author:LIN,CHIH-YI , CHU,YEN-CHIEH, LIN,WEN-HSIN**

**License:** CC-BY-4.0

**Problem Statement**

Health monitoring systems increasingly rely on ECG signals to estimate
heart rate variability (HRV) and detect abnormalities.\
When monitoring multiple users simultaneously, significant individual
differences exist in resting heart rate, baseline HRV, and ECG signal
noise patterns.

Current systems often apply a single fixed ECG analysis pipeline to all
users. This approach can lead to misclassification, where valid ECG
segments are incorrectly judged as abnormal or unreliable, resulting in
unnecessary manual re-examination and delayed analysis.

**Context / Background**

- Each monitored user generates 30--50 ECG segments per day

- Typical segment length ranges from 30 to 60 seconds

- ECG signal quality varies due to motion, sensor placement, and
  individual physiology

- HRV metrics are highly sensitive to R-peak detection accuracy

- Manual inspection is still required when automated analysis fails

**Analysis**

**Root Causes**

1.  Significant inter-subject variability in heart rate and HRV
    baselines

2.  ECG waveform morphology differs across individuals

3.  Fixed thresholds and processing parameters fail to generalize across
    users

4.  Noise characteristics vary depending on activity and sensor
    conditions

**Constraints**

- The system must support simultaneous monitoring of multiple
  individuals

- Automated analysis must remain explainable and auditable

- Manual intervention should be minimized but not eliminated

- The system must scale without redesign when new users are added

**Requirements**

- Real-time or near real-time ECG processing

- Personalized interpretation of ECG and HRV metrics

- Adaptive strategy selection rather than a single fixed pipeline

- Robust handling of noisy or low-quality signals

**Proposed Approach (Chat-Based)**

A human-in-the-loop workflow where a user:

1.  **Inputs** individual-specific information (sampling rate, expected
    heart rate range) into a large language model (LLM)

2.  **Uploads** ECG signal segments manually via chat

3.  **Receives** HRV analysis results and recommendations

4.  **Re-enters** individual context when the LLM loses track

5.  **Manually verifies** whether the results are reasonable

6.  **Repeats** the process for each ECG segment and individual

**Observed Limitations**

- High repetitive workload due to manual data input

- Loss of individual context across interactions

- Difficulty handling multiple individuals simultaneously

- Fixed analysis strategies with limited adaptability

- Limited time savings compared to manual analysis

**Proposed Approach (Agentic)**

An AI agent-based system capable of autonomous, adaptive ECG analysis.

**Workflow**

1.  **ECG Ingestion Module**

    - Receives ECG segments along with a unique subject identifier

    - Standardizes format and performs basic preprocessing

2.  **Personal Profile Module**

    - Retrieves historical heart rate, RR interval, and HRV
      distributions

    - Stores previously successful analysis strategies per individual

3.  **Agent Decision Module**

    - Selects appropriate filtering and R-peak detection strategies

    - Adjusts parameters based on signal quality and individual
      characteristics

    - Retries analysis when results are physiologically implausible

4.  **HRV Evaluation Module**

    - Computes HRV metrics such as SDNN, RMSSD, and LF/HF

    - Validates results against individual-specific physiological ranges

5.  **Decision Module**

    - Accepts reliable results and updates personal profiles

    - Rejects unusable segments and logs failure reasons

6.  **Logging and Monitoring Module**

    - Tracks retry counts, failure causes, and performance metrics

    - Supports system maintenance and continuous improvement

**Expected Outcomes**

- Reduced false-positive ECG rejections across individuals

- Improved HRV stability within the same subject

- Lower manual review workload for clinicians or technicians

- Scalable ECG analysis as the number of monitored users increases

- More reliable and personalized HRV estimation
