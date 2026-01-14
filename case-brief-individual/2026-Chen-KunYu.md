# Case Brief: Agentic Code Flow & Fatigue Assistant

**Author:** 2026-Chen-KunYu
**License:** CC-BY-4.0

## Problem Statement

Programmers often experience "tunnel vision" during development, ignoring physical signs of fatigue or high stress. Continuing to code under cognitive overload frequently leads to logical blind spots, increased bug rates, and "ineffective overtime."

Crucially, when developers are fatigued, they often lack the motivation to organize code or write proper commit messages. This leads to "abandoned work"—leaving the workspace without committing changes, resulting in an unstable project state and untracked progress.

## Context/Background

-   **Industry Context:** Software development requires sustained high cognitive load. "Burnout" and "Technical Debt" are significant issues in the industry.
-   **Current Solutions:** Existing tools like Pomodoro timers or smartwatches are passive or purely time-based. They lack "context awareness" (don't know if the user is deep in code) and cannot actively assist in the workflow.
-   **Stakeholders:** Software engineers, Engineering managers (concerned with code quality), and HR (concerned with employee health).
-   **The Gap:** There is a lack of intelligent assistants that perceive both "physiological state" and "work context" to proactively assist in wrapping up chaotic code, thereby lowering the psychological barrier to stopping work.

## Analysis

### Root Causes

1.  **Lack of Self-Awareness:** Users often do not realize their cognitive decline until it is too late (tunnel vision).
2.  **High Friction in Wrapping Up:** Writing commit messages and organizing code requires significant mental effort, which is depleted when fatigued.
3.  **Disconnect between Health and Workflow:** Health data (ECG) and Work data (Git/IDE) exist in silos.

### Constraints

-   **Non-Intrusive:** The solution must not forcefully interrupt the user's flow in a way that causes frustration.
-   **Privacy:** Physiological data (ECG) must be handled securely.
-   **Accuracy:** The system must distinguish between "good flow" and "fatigued tunnel vision."

### Requirements

-   **Multi-modal Sensing:** Must combine physiological signals (ECG/HRV) with digital footprints (IDE focus, Git status).
-   **Generative Capability:** Must be able to "ghostwrite" commit messages to reduce the burden on the user.
-   **Closed-Loop Interaction:** Needs a feedback mechanism (e.g., Snooze vs. Rest) to adapt to user needs.

## Proposed Approach (Chat-based)

_Note: This approach describes how a user would solve this problem using a standard LLM chatbot (e.g., ChatGPT) manually._

A programmer could:

1.  **Self-Monitor:** Rely on subjective feelings to realize they are tired.
2.  **Collect Context:** Manually run `git diff` in the terminal and copy the output.
3.  **Interact:** Paste the diff into ChatGPT with a prompt like "Summarize these changes into a git commit message so I can rest."
4.  **Execute:** Copy the generated message back to the terminal and execute `git commit`.

_Limitation:_ This requires high self-awareness and manual effort, which is exactly what a fatigued user lacks.

## Proposed Approach (Agentic)

_Note: This approach describes the autonomous solution proposed in the project._

An Agentic AI system ("Code Flow Assistant") would:

1.  **Perceive (Sense):** Continuously monitor ECG trends (using WESAD-derived features) for signs of fatigue _and_ monitor Git status for uncommitted changes.
2.  **Reason (Think):** Analyze the combination of data.
    -   _Logic:_ "User is physiologically fatigued + High volume of uncommitted code = Risk of abandoned work."
    -   _Decision:_ Trigger a gentle intervention to offer "Ghostwriting" services.
3.  **Act (Execute):**
    -   Proactively notify the user via a smart widget.
    -   **Tool Use:** Autonomous call to `git diff` to retrieve changes.
    -   **GenAI Process:** Send changes to an LLM to generate a WIP (Work In Progress) commit message.
    -   **Git Action:** Execute `git commit` automatically upon user confirmation.
4.  **Adapt:** Learn from user feedback (e.g., if the user hits "Snooze," enter a tighter supervision loop).

## Expected Outcomes

-   **Reduce "Abandoned Work":** Ensure code is in a "Clean State" (committed) before every break.
-   **Improve Self-Awareness:** Help developers recognize their own physiological limits before burnout occurs.
-   **Atomic Habits:** Reduce the bad habit of hoarding changes due to laziness in writing commit messages.
-   **Non-Coercive Intervention:** Maintain user control while guiding healthier work habits.

## References

1.  Schmidt, P., Reiss, A., Duerichen, R., Marberger, C., & Van Laerhoven, K. (2018). Introducing WESAD, a multimodal dataset for wearable stress and affect detection.
