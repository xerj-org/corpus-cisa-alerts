---
title: "Poland Energy Sector Cyber Incident Highlights OT and ICS Security Gaps"
type: alert
date: 2026-02-10
source: https://www.cisa.gov/news-events/alerts/2026/02/10/poland-energy-sector-cyber-incident-highlights-ot-and-ics-security-gaps
---
_The purpose of this Alert is to amplify Poland’s Computer Emergency Response Team (CERT Polska’s) Energy Sector Incident Report published on Jan. 30, 2026, and highlight key mitigations for Energy Sector stakeholders._

In December 2025, a malicious cyber actor(s) targeted and compromised operational technology (OT) and industrial control systems (ICS) in Poland’s Energy Sector—specifically renewable energy plants, a combined heat and power plant, and a manufacturing sector company—in a cyber incident. The malicious cyber activity highlights the need for critical infrastructure entities with vulnerable edge devices to act now to strengthen their cybersecurity posture against cyber threat activities targeting OT and ICS.

A malicious cyber actor(s) gained initial access in this incident through vulnerable internet-facing edge devices, subsequently deploying wiper malware and causing damage to remote terminal units (RTUs). The malicious cyber activity caused loss of view and control between facilities and distribution system operators, destroyed data on human machine interfaces (HMIs), and corrupted system firmware on OT devices. While the affected renewable energy systems continued production, the system operator could not control or monitor them according to their intended design.[1](https://www.cisa.gov/news-events/alerts/2026/02/10/poland-energy-sector-cyber-incident-highlights-ot-and-ics-security-gaps#Note1)

CERT Polska’s incident report highlights:

*   Vulnerable edge devices remain a prime target for threat actors. 
    *   As indicated by CISA’s [Binding Operational Directive (BOD) 26-02: Mitigating Risk From End-of-Support Edge Devices](https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices), end-of-support edge devices pose significant risks.

*   OT devices without firmware verification can be permanently damaged. 
    *   Operators should prioritize updates that allow firmware verification when available; if updates are not immediately feasible, ensure that cyber incident response plans account for inoperative OT devices to mitigate prolonged outages.

*   Threat actors leveraged default credentials, a vulnerability not limited to specific vendors, to pivot onto the HMI and RTUs. 
    *   Operators should immediately change default passwords and establish requirements for integrators or OT suppliers to enforce password changes in the future.

CISA and the Department of Energy’s Office of Cybersecurity, Energy Security, and Emergency Response (DOE CESER) urge OT asset owners and operators to review the following resources for more information about the malicious activity and mitigations:

*   CERT Polska’s [Energy Sector Incident Report - 29 December 2025](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/).
*   CISA’s joint fact sheet with FBI, EPA, and DOE [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
*   DOE’s Energy Threat Analysis Center’s threat advisories.

## **Acknowledgements**

DOE CESER and CERT Polska contributed to this Alert.

## **Disclaimer**

The information in this report is being provided “as is” for informational purposes only. CISA does not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document. Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA.

## **Notes**

1.   [](https://www.cisa.gov/news-events/alerts/2026/02/10/poland-energy-sector-cyber-incident-highlights-ot-and-ics-security-gaps)CERT Polska, “Energy Sector Incident Report - 29 December 2025,” Naukowa i Akademicka Sieć Komputerowa Poland _,_ last modified January 30, 2026, [https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/).
