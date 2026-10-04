---
title: "CISA and Partners Release Advisory Update on Akira Ransomware"
type: alert
date: 2025-11-13
source: https://www.cisa.gov/news-events/alerts/2025/11/13/cisa-and-partners-release-advisory-update-akira-ransomware
---
Today,Cybersecurity and Infrastructure Security Agency (CISA), in collaboration with the Federal Bureau of Investigation, Department of Defense Cyber Crime Center,Department of Health and Human Services, and international partners, released an updated joint Cybersecurity Advisory, [#StopRansomware: Akira Ransomware](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a "#StopRansomware: Akira Ransomware"), to provide network defenders with the latest indicators of compromise, tactics, techniques, and procedures, and detection methods associated with Akira ransomware activity.

This advisory reflects new findings as of Nov. 13, 2025, highlighting Akira ransomware’s evolution and continued threat to critical infrastructure sectors. Akira ransomware threat actors, associated with groups such as Storm-1567, Howling Scorpius, Punk Spider, and Gold Sahara, have expanded their capabilities, targeting small and medium-sized businesses as well as larger organizations across sectors including Manufacturing, Educational Institutions, Information Technology, Healthcare, Financial, and Food and Agriculture.

**Key Updates:**

*   **Initial Access**: Threat actors exploit vulnerabilities in edge devices and backup servers, such as authentication bypass, cross-site scripting, buffer overflow, and compromise credentials through brute-force techniques.
*   **Discovery**: Threat actors use command line techniques to accomplish network and domain discovery.
*   **Defense Evasion**: Threat actors use remote management and monitoring tools such as Anydesk and LogMeIn to mimic administrator activity, and modify firewall settings, terminate antivirus processes and uninstall EDR systems.
*   **Privilege Escalation**: Threat actors deploy POORTRY malware to modify BYOVD configurations on vulnerable drivers, create administrator accounts, steal administrator login credentials, and bypass VMDK protections, as well as exploit Veeam vulnerabilities.
*   **Lateral Movement**: Threat actors use remote access tools and protocols like RDP, SSH, and steal Kerberos authentication tickets to move within networks.
*   **Command and Control**: Threat actors use Ngrok to establish encrypted sessions, SystemBC malware as a remote access trojan, and STONETOP malware to deploy Akira payloads.
*   **Exfiltration and Impact**: Threat actors use protocols such as FTP, SFTP, and cloud services to exfiltrate data.
*   **Encryption**: Threat actors use a new Akira_v2 ransomware variant that enables faster encryption speeds and further inhibits system recovery.

CISA and its partners strongly encourage organizations to apply patches for known vulnerabilities, especially those affecting VPN products and backup servers, and enforce multifactor authentication for all remote access services. Organizations should monitor unauthorized domain account creation and unusual network activity while deploying endpoint detection and response solutions to enhance security.

For more information, see CISA’s updated[#StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide "#StopRansomware Guide").
