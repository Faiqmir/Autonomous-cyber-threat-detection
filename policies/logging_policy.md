# Enterprise Logging Policy Template

## 1. Purpose
The purpose of this policy is to establish a standard for the generation, transmission, storage, analysis, and disposal of system and application logs within [Organization Name]. Effective logging is critical for security monitoring, incident response, and regulatory compliance.

## 2. Scope
This policy applies to all:
- Servers (Physical and Virtual)
- Network Devices (Firewalls, Routers, Switches)
- Database Systems
- Applications (Internal and External facing)
- Cloud Infrastructure (AWS, Azure, GCP)
- Endpoints (Workstations, Laptops) - Key events

## 3. What to Log (Auditable Events)
At a minimum, the following events must be logged:

### 3.1 Authentication & Authorization
- Successful and failed login attempts (including source IP).
- Privilege escalation (sudo, runas).
- Password changes or resets.
- Group membership changes.

### 3.2 System & Data Access
- Access to critical files or databases.
- File integrity monitoring alerts (changes to system binaries).
- USB device insertion/removal (for high-security zones).

### 3.3 Network Activity
- Firewall allows/denies (ingress/egress).
- VPN connection establishment and termination.
- Remote access sessions (RDP, SSH).

### 3.4 Application Security
- Input validation failures (XSS, SQLi attempts).
- Session cookie anomalies.
- Application errors and crashes.

## 4. Log Standards & Format
- **Format**: Logs must be structured (JSON preferred) or Key-Value pairs to facilitate parsing.
- **Time Synchronization**: All systems must use NTP to synchronize time to UTC.
- **Fields**: Every log entry must contain:
  - Timestamp (ISO 8601)
  - Hostname / IP Address
  - User ID / Service Account
  - Event Source / Application Name
  - Event ID / Type
  - Severity Level

## 5. Retention Policy
| Log Type | Online Retention (Hot) | Archive Retention (Cold) | Total Retention |
| :--- | :--- | :--- | :--- |
| Security / Auth Logs | 90 Days | 1 Year | 1 Year 3 Months |
| Application Logs | 30 Days | 6 Months | 7 Months |
| Regulatory (PCI/HIPAA)| 1 Year | 6 Years | 7 Years |
| Firewall / Netflow | 7 Days | 90 Days | 97 Days |

## 6. Protection & Integrity
- Logs must be shipped to a centralized server (SIEM) in near real-time.
- Local log files should be restricted to `root` or `admin` read-only access.
- Centralized log storage must use WORM (Write Once, Read Many) technology where possible.
- Logs containing PII must be masked or encrypted.

## 7. Review & Monitoring
- Critical security logs must be monitored continuously via automated alerting.
- Regular audits of the logging infrastructure must be performed quarterly.

## 8. Violation & Enforcement
Failure to comply with this policy may result in disciplinary action up to and including termination of employment.
