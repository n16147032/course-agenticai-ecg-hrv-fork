# Case Brief: Inefficient Analysis of Holter Monitor Data

**Author:** Saquib Rafiq

---

## Problem Definition

The Cardiology Department processes approximately **20 Holter Monitor recordings per day**.  
Each recording contains **24 hours of continuous ECG data**, approximately **100,000 heartbeats**.

Currently, these files are **manually reviewed by Cardiac Technicians** to identify intermittent arrhythmias.

### Department Resources

- **5 Cardiac Technicians**
- Average fully loaded cost: **$50 per hour**

### Data Characteristics Per Recording

- **99% Normal Sinus Rhythm**
  - Medically irrelevant
  - Requires ~30 minutes of scrolling to verify and discard
- **1% Critical Events**
  - Examples: short HRV drop, cardiac pause
  - Drives diagnosis and clinical decision making

---

## Current Cost of Manual Review

### Time Wasted Per Day

```
20 files × 99% normal data × 30 minutes
= 594 minutes ≈ 9.9 hours per day
```

### Workforce Impact

- Equivalent to **1.25 full time technicians**
- Paid primarily to scroll through normal ECG data

### Daily Cost

```
9.9 hours × $50/hour = $495 per day
```

### Annual Cost (250 workdays)

```
$495 × 250 = $123,750 per year
```

### Additional Risk

- Increased **human fatigue**
- Potential to miss subtle but critical arrhythmias

---

## Expected Outcome

### Key Properties of the Proposed Solution

- **Local AI Model Operation**
  - Batch processor on completed 24 hour CSV files
  - Python based HRV analysis on every heartbeat
  - Segment classification into Normal or Critical

- **Automatic Filtering**
  - ~23.5 hours archived as Normal
  - ~30 minutes of relevant data surfaced

- **Targeted Reporting**
  - One page Highlight Reel
  - Top 5 Critical Events ranked by lowest HRV

- **Event Quality**
  - ~90% true arrhythmias
  - ~10% dismissible artifacts

- **System Maintenance**
  - Senior technician validation
  - ~30 minutes per week

---

## Expected Reduction in Work Hours

| Task | Before | After |
|---|---|---|
| Scrolling normal data | ~10 hrs/day | ~0.5 hrs/day |
| Analyzing critical events | Included | ~1.5 hrs/day |
| **Total reduction** |  | **~8 hrs/day** |

---

## Expected Cost Reduction

- **AI assisted analysis cost:** ~$15,000 per year  
- **Current manual review cost:** ~$123,750 per year  

### Annual Savings

```
$123,750 − $15,000 = $108,750 per year
```

---

## Solution Proposal (Chat Based Attempt)

### Intended Workflow

1. Open 24 hour CSV file in Excel  
2. Open a web based LLM  
3. Copy paste ECG data into chat  

### Failure Points

- Token limit exceeded
- HIPAA privacy violation risk
- No local processing

### Result

Manual review remains unavoidable.
