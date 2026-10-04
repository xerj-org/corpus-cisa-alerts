---
title: "CISA Urges Hardening Fortinet Devices After Reports of Credential Exposure"
type: alert
date: 2026-06-22
source: https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure
revision: "June 22, 2026"
---
**Update June 22, 2026:**  
_CISA has updated this Alert to incorporate the link to Fortinet’s recent guidance on this activity._

CISA is aware of global reports that malicious cyber actors have targeted internet-accessible Fortinet devices across government and private sector organizations using compromised credentials. This activity, referred to as FortiBleed, involves the exposure of leaked credentials associated with approximately 74,000 Fortinet devices, including firewalls and virtual private network (VPN) gateways.

To defend against this malicious cyber activity, CISA urges impacted Fortinet customers with FortiGate appliances and associated secure sockets layer (SSL) VPN gateways to immediately:

1.   **Terminate sessions and reset credentials.** Terminate all active SSL VPN and administrative sessions. Reset all Fortinet VPN and administrative passwords, especially on internet-facing systems, and enforce strong password policies.
2.   **Ensure secure credential storage.** Confirm your organization’s use of the Password-Based Key Derivation Function 2 (PBKDF2) algorithm to store administrator credentials and remove weaker legacy hashes per Fortinet’s guidance (see, [Fortinet's Technical Tip: Enforcing PBKDF2 as hash function for administrator accounts in FortiOS v7.2.11 and later](https://community.fortinet.com/fortigate-3/technical-tip-enforcing-pbkdf2-as-hash-function-for-administrator-accounts-in-fortios-v7-2-11-and-later-220652)). 
3.   **Review logs.** Review firewall, VPN, authentication, and domain controller logs for lateral movement, unusual access, suspicious accounts, or unauthorized configuration changes.
4.   **Enable phishing-resistant multifactor authentication (MFA).**[Require phishing-resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf) on all remote access and administrative accounts and ensure it is enforced on all external gateways and administrative interfaces.
5.   **Reduce the attack surface and lock down management access.** Ensure the administration of your firewall is inaccessible from the public internet; restrict Fortinet management interfaces to trusted internal networks; and remove or disable any unauthorized or unnecessary accounts.

See the following resources to determine your organization’s potential impact and find additional guidance on the credentials compromised:

*   Tech Times: [Fortinet FortiGate Credential Leak Hits 73,932 Firewalls: Half the Internet-Facing Fleet](https://www.techtimes.com/articles/318599/20260618/fortinet-fortigate-credential-leak-hits-73932-firewalls-half-internet-facing-fleet.htm)
*   SOCRadar: [FortiBleed: The Compromise of 80,000+ Fortinet Firewalls](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)
*   Hudson Rock: [FortiBleed: 75,000 Fortinet Firewalls Compromised: Global Enterprises Exposed – Claim Your Ethical Disclosure](https://www.hudsonrock.com/blog/fortibleed-75000-fortinet-firewalls-compromised-global-enterprises-exposed-claim-your-ethical-disclosure)
*   Arctic Wolf: [Active FortiBleed Campaign Impacting Fortinet Devices Across 194 Countries](https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/)
*   Fortinet: [Attacks at the Speed of AI](https://www.fortinet.com/blog/industry-trends/attacks-at-the-speed-of-ai)
*   Fortinet: [Analysis of Reported Credential Compromise of FortiGate Devices](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)

## **Disclaimer**

The information in this report is being provided “as is” for informational purposes only. CISA does not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document. Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA.
