# Case Brief - Individual Submission and Group Submission

This folder contains individual case briefs written by each student and each groups final case brief.

## Requirements

### File Format

- **Format:** Markdown (`.md`)
- **Naming Individual:** `YYYY-FamilyName-FirstName.md` (ASCII characters only)
- **Naming Group:** `YYYY-FamilyName1-FamilyName2-FamilyName3.md` (ASCII characters only)
- **License:** Include license declaration (CC-BY-4.0 recommended)

First each student submit their own case brief, after discussing and reaching consensus the group submits its case brief. Updates to the group case brief are allowed until the implementation is presented.

### Content Requirements

A case brief is a structured analysis document that:

1. **Identifies a real-world problem** suitable for an AI agent solution
2. **Analyzes the problem** systematically
3. **Proposes an approach** using agentic AI concepts

Your case brief must include:

| Section | Description |
|---------|-------------|
| **Title** | Clear, descriptive title of the case |
| **Problem Statement/Definition** | What problem are you addressing? Why does it matter? |
| **Context/Background** | Industry context, stakeholders, current solutions, cost |
| **Analysis** | Root cause analysis, constraints, requirements |
| **Proposed Approach/Solution proposal** | How can you solve it using a Chat-based AI, e.g. ChatGPT? How could an AI agent address this problem? |
| **Expected Outcomes** | What would success look like? |
| **References** | Sources cited (if any) |

### Length
- Approximately 1-2 pages (500-1000 words)
- Quality over quantity

---

## Grading Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Problem Description | 40% | Clarity, specificity, and relevance of the problem |
| Analysis Quality | 40% | Depth of analysis, logical reasoning, consideration of constraints |
| Proposed Approach | 15% | Feasibility and alignment with agentic AI concepts |
| Writing Quality | 5% | Clear structure, grammar, formatting |

Scoring is relative to the example brief provided by the instructor.

---

## Example Case Brief

```markdown
# Case Brief: Automated Patient Triage in Emergency Departments

**Author:** 2026-Example-Student
**License:** CC-BY-4.0

## Problem Statement

Emergency departments (EDs) face increasing patient volumes while maintaining
limited staff. Triage—the process of prioritizing patients by severity—is
critical but time-consuming. Delays in triage can lead to adverse outcomes
for high-acuity patients.

## Context/Background

- Average ED wait times exceed 2 hours in urban hospitals
- Triage nurses spend 5-10 minutes per patient assessment
- Misclassification rates range from 10-30% depending on experience
- Current electronic health record (EHR) systems provide limited decision support

## Analysis

### Root Causes
1. High patient-to-nurse ratios during peak hours
2. Subjective assessment varies by nurse experience
3. Information overload from multiple data sources (vitals, history, symptoms)

### Constraints
- Must integrate with existing EHR systems
- Cannot replace clinical judgment (regulatory requirements)
- Must handle edge cases safely (fail-safe design)

### Requirements
- Real-time processing of patient data
- Explainable recommendations (not black-box)
- Continuous learning from outcomes

## Proposed Approach (Chat-based)

A nurse could:
1. **Collect** patient data from multiple sources (vitals monitors, intake forms) and copy-paste them into the chat with a standardised prompt
2. **Analyze** using the inputed data and prompt
3. **Recommend** priority level with explanation
4. **Learn** by updating the standardised prompt based on nurse feedback and patient outcomes

## Proposed Approach (Agentic)

An AI agent system could:
1. **Collect** patient data from multiple sources (vitals monitors, intake forms)
2. **Analyze** using trained models on historical triage outcomes
3. **Recommend** priority level with explanation
4. **Learn** from nurse feedback and patient outcomes

The agent would augment (not replace) nurse decision-making, flagging
high-risk cases for immediate attention.

## Expected Outcomes

- 30% reduction in triage time
- Improved consistency in priority assignment
- Early warning for deteriorating patients
- Reduced cognitive load on triage nurses

## References

1. Fernandes M, Vieira SM, Leite F, Palos C, Finkelstein S, Sousa JMC. Clinical Decision Support Systems for Triage in the Emergency Department using Intelligent Systems: a Review. Artif Intell Med. 2020 Jan;102:101762. doi: 10.1016/j.artmed.2019.101762. PMID: 31980099.
2. Giordano P, D'Ambrosio M, Banushaj M, Pizzolo C, Iotti LM, Voci R. ChatGPT e il suo utilizzo nel supporto decisionale clinico: una scoping review. Recenti Prog Med. 2024 Nov;115(11):560-561. Italian. doi: 10.1701/4365.43602. PMID: 39550663.
3. WHO Emergency care system framework. url: https://www.who.int/publications/i/item/who-emergency-care-system-framework (Accessed 2026-01-13)
```

---

## How to Create a Markdown File

### Option 1: Text Editor

Use any text editor (VS Code, Notepad++, Sublime Text) and save with `.md` extension.

### Option 2: Online Editor or AI

Use an online Markdown editor like:
- https://dillinger.io/
- https://stackedit.io/
- Almost all large language models can output Markdown when instructed to do so (tips: ask them to provide it in a code block)

### Markdown Basics

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another point

1. Numbered item
2. Another item

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |

[Link text](https://example.com)
```

---

## Submission Checklist

Before submitting, verify:

- [ ] File named correctly: If individual, then `YYYY-FamilyName-FirstName.md`, otherwise `YYYY-FamilyName1-FamilyName2-FamilyName3.md` (Capital first letter only)
- [ ] Only ASCII characters in filename
- [ ] License declaration included
- [ ] All required sections present
- [ ] No personally identifiable information (PII)
- [ ] Proofread for clarity and grammar by an LLM
