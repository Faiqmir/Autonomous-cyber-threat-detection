# Establishing Security Baselines

## Overview
Baselining is the process of defining "normal" behavior for your network, systems, and users. Anomalies—deviations from this baseline—are often the first indicator of a compromise.

## 1. User Behavior Analytics (UBA)
### What to profile:
- **Login Times**: Create a profile of standard working hours for each user. Flag logins at 3 AM for a 9-5 employee.
- **Geography**: Map identifying standard login locations (City/Country). Flag logins from unexpected countries (Impossible Travel).
- **Resource Access**: Track which servers/files a user normally accesses. Flag access to the "Finance" folder by an Engineer.

### Implementation Method:
1. **Data Collection**: Collect 30 days of authentication logs.
2. **Analysis**: Use Python/pandas or Splunk's `stats` command to calculate mean and standard deviation for login counts/times.
3. **Thresholding**: Alert on activity > 3 standard deviations from the mean.

## 2. System Performance & Activity
### What to profile:
- **Process List**: distinct list of running processes on a "Gold Image" server. Flag any unknown binary.
- **Network Connections**: Standard outbound connections (e.g., DNS, Windows Updates). Flag connections to unknown IPs on high ports.
- **Service Accounts**: Identify which mechanisms (Cron, Task Scheduler) are normally used.

## 3. Baseling Steps
1. **Scope Phase**: Select a specific group (e.g., Domain Controllers) or user group (e.g., Domain Admins).
2. **Observation Phase**: Run in "Learning Mode" for 2-4 weeks. Do not alert, just record.
3. **Analysis Phase**: Review the data. Filter out known legitimate variability (e.g., Patch Tuesday).
4. **Lockdown Phase**: Convert observed patterns into exclusion rules. Everything else becomes an alert.
