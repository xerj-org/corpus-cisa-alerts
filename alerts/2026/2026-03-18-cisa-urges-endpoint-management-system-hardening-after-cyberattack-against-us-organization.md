---
title: "CISA Urges Endpoint Management System Hardening After Cyberattack Against US Organization"
type: alert
date: 2026-03-18
source: https://www.cisa.gov/news-events/alerts/2026/03/18/cisa-urges-endpoint-management-system-hardening-after-cyberattack-against-us-organization
---
CISA is aware of malicious cyber activity targeting endpoint management systems of U.S. organizations based on the March 11, 2026 cyberattack against U.S.-based medical technology firm Stryker Corporation, which affected their Microsoft environment.[1](https://www.cisa.gov/news-events/alerts/2026/03/18/cisa-urges-endpoint-management-system-hardening-after-cyberattack-against-us-organization#note1) To defend against similar malicious cyber activity, CISA urges organizations to harden endpoint management system configurations using the recommendations and resources provided in this alert. CISA is conducting enhanced coordination with federal partners, including the Federal Bureau of Investigation (FBI), to identify additional threats and determine mitigation actions.

To defend against similar malicious activity that misuses legitimate endpoint management software, CISA urges organizations to implement Microsoft’s newly released [best practices for securing Microsoft Intune](https://techcommunity.microsoft.com/blog/intunecustomersuccess/best-practices-for-securing-microsoft-intune/4502117); the principles of these recommendations can be applied to Intune and more broadly to other endpoint management software:

*   **Use principles of least privilege when designing administrative roles**. 
    *   Leverage Microsoft Intune’s role-based access control (RBAC) to assign the minimum permissions necessary to each role for completing day-to-day operations—permissions include what actions the role can take, and what users and devices it can apply that action to.

*   **Enforce phishing-resistant multi-factor authentication (MFA) and privileged access hygiene**. 
    *   Use Microsoft Entra ID capabilities (including Conditional Access, MFA, risk signals, and privileged access controls) to block unauthorized access to privileged actions in Microsoft Intune.

*   **Configure access policies to require**[**Multi Admin Approval in Microsoft Intune**](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/multi-admin-approval). 
    *   Set up policies that require a second administrative account’s approval to allow changes to sensitive or high-impact actions (such as device wiping), applications, scripts, RBAC, configurations, etc. 

Additionally, CISA recommends reviewing the following resources to strengthen defenses against similar malicious cyber activity:

*   Microsoft resources: 
    *   For recommendations on securing Microsoft Intune, see [Best practices for securing Microsoft Intune](https://techcommunity.microsoft.com/blog/intunecustomersuccess/best-practices-for-securing-microsoft-intune/4502117).
    *   For guidance on implementing Multi Admin Approval in Microsoft Intune, see [Use Access policies to implement Multi Admin Approval](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/multi-admin-approval).
    *   For recommendations on configuring Microsoft Intune using zero trust principles, see [Configure Microsoft Intune for increased security](https://learn.microsoft.com/en-us/intune/intune-service/protect/zero-trust-configure-security?toc=/security/zero-trust/assessment/toc.json&bc=/security/zero-trust/assessment/toc.json).
    *   For guidance on implementing Microsoft Intune RBAC policies, see [Role-based access control (RBAC) with Microsoft Intune](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/role-based-access-control).
    *   For guidance on deploying Privileged Identity Management (PIM) across Microsoft Intune, Entra ID, and other Microsoft software, see [Plan a Privileged Identity Management deployment](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan). 

*   CISA resources: 
    *   For guidance on implementing phishing-resistant multifactor authentication (MFA), see [Implementing Phishing-Resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf).

## **Disclaimer**

The information in this report is being provided “as is” for informational purposes only. CISA does not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document. Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA.

## **Acknowledgements**

Microsoft and Stryker contributed to this alert.

## **Notes**[](https://www.cisa.gov/news-events/alerts/2026/03/18/cisa-urges-endpoint-management-system-hardening-after-cyberattack-against-us-organization)

1 For updates from Stryker on the incident, see “Customer Updates: Stryker Network Disruption,” Stryker, last modified March 15, 2026, [https://www.stryker.com/us/en/about/news/2026/a-message-to-our-customers-03-2026.html](https://www.stryker.com/us/en/about/news/2026/a-message-to-our-customers-03-2026.html).
