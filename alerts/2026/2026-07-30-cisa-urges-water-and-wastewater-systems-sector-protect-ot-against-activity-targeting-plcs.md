---
title: "CISA Urges Water and Wastewater Systems Sector to Protect OT Against Activity Targeting PLCs"
type: alert
date: 2026-07-30
source: https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs
co-published: "NCSC-UK"
---
CISA is currently observing a significant increase in cyber threat actors targeting programmable logic controllers (PLCs) in the Water and Wastewater Systems (WWS) Sector. CISA urges critical infrastructure owners, operators, and integrators to remove publicly exposed PLCs and other operational technology (OT) from the internet as soon as possible. Threat actors targeting exposed PLCs have modified passwords to lock out operators and disconnected the PLCs by changing their IP addresses. This activity has resulted in boil water notices and sustained manual operations.

These threat actors are targeting water entities of all sizes. Even water organizations with mature cybersecurity processes should validate their external connections, as this targeting activity includes cellular modems installed by operators, vendors, or system integrators that may not be documented or included in routine attack surface scans. OT assets exposed to the internet have an increased risk of defacement, configuration changes, operational disruptions, and, in severe cases, physical damage.

CISA recommends organizations implement the following mitigations:

*   Disconnect the PLC from the internet. Remote access for operational purposes should go through a VPN or gateway device, not directly to the PLC.
*   Enable password protection and change default passwords.
*   Allowlist IPs to only allow remote access from known engineering laptops or other critical OT assets.

After disconnecting PLCs from the internet, operators should ensure they have a known clean backup of the PLC image in case they are locked out by a modified password. **Note:**Owners, operators, and integrators of Rockwell Automation MicroLogix 1400 PLCs should see Rockwell Automation’s [IMPORTANT NOTICE: Restoring Access to a MicroLogix™ 1400 Controller When the Password Is Unknown](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1790.html) for guidance addressing this activity.

To securely enable remote access to your OT systems, CISA recommends system owners, operators, and integrators see the following resources for guidance:

*   CISA: [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)
*   United Kingdom's National Cyber Security Center: [Secure Connectivity Principles for Operational Technology](https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity)
*   Federal Bureau of Investigation (FBI): [Malicious Cyber Actors Targeting Water and Wastewater Sector Internet Facing Programmable Logic Controllers, Causing Operational Disruptions](https://www.ic3.gov/PSA/2026/PSA260730.pdf)

For additional support, contact the Environmental Protection Agency’s [Cybersecurity Technical Assistance Program for the Water Sector](https://www.epa.gov/cyberwater/forms/cybersecurity-technical-assistance-program-water-sector) or your [CISA Regional Office](https://www.cisa.gov/about/regions).

To report a cyber incident, contact CISA’s 24/7 Operations Center ([contact@cisa.dhs.gov](mailto:contact@cisa.dhs.gov)), or call 1-844-Say-CISA (1-844-729-2472). Please see [Reporting a Cyber Incident](https://www.cisa.gov/reporting-cyber-incident) for more details or contact [FBI’s Internet Crime Complaint Center (IC3)](https://www.ic3.gov/) or your [local FBI field office](https://www.fbi.gov/contact-us/field-offices).

When available, please include the following information regarding the incident:

*   Date, time, and location of the incident
*   Type of activity
*   Number of people affected
*   Type of equipment used for the activity
*   Name of the submitting company or organization, and a designated point of contact

## **Disclaimer**

The information in this report is being provided “as is” for informational purposes only. CISA does not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document. Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA.

## **Acknowledgements**

The Environmental Protection Agency and the Federal Bureau of Investigation contributed to this Alert.
