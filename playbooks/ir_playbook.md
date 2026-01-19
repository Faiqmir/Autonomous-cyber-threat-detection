# Incident Response Playbook: Ransomware / Malware

## 1. Preparation
- **Tools**: Ensure EDR (Endpoint Detection & Response) is active.
- **Access**: Verify Admin access to Active Directory, Firewalls, and Backups.
- **Communication**: Establish out-of-band communication (Signal/WhatsApp) in case email is compromised.

## 2. Detection & Analysis
- **Trigger**: SIEM Alert "Suspicious PowerShell Download" or EDR Alert "Ransomware Behavior".
- **Triage**:
  - Is the host a critical asset? (Check `assets/critical_assets.csv`)
  - Is data being encrypted?
  - Is there lateral movement traffic?
- **Analysis Steps**:
  1. Isolate the host from the network IMMEDIATELY.
  2. Capture RAM dump if possible (for key retrieval).
  3. Identify the entry point (Phishing? RDP?).

## 3. Containment
- **Short Term**: Disconnect network cable / Disable virtual NIC.
- **Long Term**: 
  - Block C2 (Command & Control) IPs on the Firewall.
  - Reset passwords for compromised accounts (Force logout).
  - Disable File Shares (SMB) temporarily if spreading via shares.

## 4. Eradication
- Re-image the infected machine. **DO NOT TRUST A CLEANED MACHINE.**
- Patch the vulnerability used for entry (e.g., update VPN concentrator).
- Remove malicious artifacts (Scheduled tasks, Registry keys) from the network.

## 5. Recovery
- Restore data from **offline** backups (verify backups are clean first).
- Phased return to operations: Enable critical services first.
- Monitor closely for re-infection (24-48 hours).

## 6. Post-Incident Activity (Lessons Learned)
- Conduct a "Hot Wash" meeting within 72 hours.
- Update this playbook with gaps found.
- Update Detection Rules to catch this specific variant earlier next time.
