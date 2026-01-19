# Log Integrity & Security Best Practices

## Overview
Ensuring the integrity and confidentiality of logs is paramount. Attackers often attempt to delete or modify logs to cover their tracks. This document outlines the controls to prevent such actions.

## 1. Transmission Security (Data in Transit)
- **Encryption**: All log transmission must occur over encrypted channels (TLS 1.2 or higher).
- **Mutual Authentication (mTLS)**: Where possible, use mTLS between log forwarders (e.g., Filebeat) and collectors (e.g., Logstash) to ensure only authorized endpoints can send logs.

## 2. Storage Security (Data in Rest)
- **Access Control**:
  - Implement fine-grained Role-Based Access Control (RBAC) on the SIEM.
  - Analysts should have `read-only` access.
  - Only Administrators should have write access to configuration (not data).
- **Encryption**: Logs should be encrypted at rest using AES-256.

## 3. Immutability (WORM)
- **Write Once, Read Many (WORM)**: Critical logs must be stored on WORM-compliant storage media. This prevents modification or deletion even by administrative users until the retention period expires.
- **S3 Object Lock**: For cloud storage, use AWS S3 Object Lock in "Compliance Log" mode.

## 4. Integrity Verification
- **Hashing**: Logs should be hashed (SHA-256) upon ingestion.
- **Chaining**: Use blockchain or hash-chaining techniques to link log entries, making it impossible to remove a single entry without breaking the chain.
- **Canary Logs**: Inject artificial "canary" log entries periodically and verify their existence to detect mass deletion events.

## 5. Network Segmentation
- **Management Plane**: The logging infrastructure (SIEM, Collectors) should reside in a segregated high-security network zone, accessible only via a Jump Box or specific VPN.
