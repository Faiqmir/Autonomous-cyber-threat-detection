# Threat Landscape & Log Source Mapping

## Overview
This document maps potential cyber threats relevant to the organization against the specific log sources required to detect them. This ensures that our logging strategy is threat-informed.

## Threat: Ransomware
**Description**: Malware that encrypts files and demands payment for the decryption key, often involving lateral movement and data exfiltration.

| Attack Stage (MITRE ATT&CK) | Indicators of Compromise (IoCs) | Required Log Source | Detection Logic |
| :--- | :--- | :--- | :--- |
| **Initial Access** | Phishing attachment, RDP Brute Force | Email Gateway, VPN Logs, Windows Event 4625 | High volume of failed logins in short time. |
| **Execution** | Suspicious PowerShell scripts, Unknown Binaries | PowerShell (Event 4104), Sysmon (Event 1) | Execution of encoded PowerShell commands. |
| **Lateral Movement** | SMB/Admin Share access, PsExec | Windows Security (4624 type 3), Firewall internal traffic | Workstation-to-Workstation traffic on port 445. |
| **Impact** | Mass file modification, Shadow Copy Deletion | File Integrity Monitoring, Windows System (Event 7036 - VSS stop) | `vssadmin delete shadows` command execution. |

## Threat: Insider Threat (Data Exfiltration)
**Description**: An authorized user abusing privileges to steal sensitive data.

| Attack Stage | Indicators of Compromise (IoCs) | Required Log Source | Detection Logic |
| :--- | :--- | :--- | :--- |
| **Collection** | Accessing sensitive folders usually untouched | File Server Audit Logs | User accessing > 50 sensitive files in 1 minute. |
| **Exfiltration** | Large file uploads to cloud storage, USB usage | Web Proxy / Firewall, Endpoint (USB mount) | Upload > 100MB to personal-drive.com. |

## Threat: Web Application Attack
**Description**: Exploiting vulnerabilities in public-facing web apps (SQLi, XSS, RCE).

| Attack Stage | Indicators of Compromise (IoCs) | Required Log Source | Detection Logic |
| :--- | :--- | :--- | :--- |
| **Reconnaissance** | Vulnerability scanning (Nmap, Nikto) | WAF Logs, Web Server Access Logs | Single IP generating 404s for various paths. |
| **Exploitation** | SQL Injection patterns in URL/Body | WAF Logs, App Error Logs | `UNION SELECT` or `' OR 1=1` in query params. |
| **Persistence** | Webshell creation | File Integrity Monitoring, Web Verification | New `.php` or `.jsp` file created in static dirs. |
