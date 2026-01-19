# Detection Rule Tuning Process

## Overview
No detection rule is perfect on day one. Tuning is the iterative process of refining rules to minimize False Positives (FP) while maintaining False Negative (FN) rates low.

## The Tuning Lifecycle

### 1. Deployment (Day 0)
- Deploy the rule in "Alert Only" or "Shadow Mode" (do not block).
- Tag alerts with "Status: Review".

### 2. Initial Review (Day 1-7)
- Review the volume of alerts generated.
- **High Volume?** (>10/day): The rule is likely too broad.
- **Investigation**: Check the first 10-20 alerts. Are they malicious?
  - **Yes**: Rule is working.
  - **No (Legitimate Admin Activity)**: Identify unique attributes of the admin activity (e.g., Specific Source IP, Specific User Group, Specific Process Path).

### 3. Exception Management
Modify the rule to exclude the confirmed benign activity.

**Example (Sigma):**
```yaml
detection:
    selection:
        ...
    filter_admins:
        User: 'DOMAIN\AdminService'
        CommandLine|contains: 'approved_script.ps1'
    condition: selection and not filter_admins
```

### 4. Continuous Feedback
- **SOC Analyst Feedback**: Create a feedback loop where analysts can flag an alert as "False Positive" easily in the case management system.
- **Quarterly Review**: Review the efficacy of all rules every 3 months. Retire rules that have never triggered (they might be broken or the threat has evolved).
