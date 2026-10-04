---
title: "Supply Chain Compromises Impact Nx Console and GitHub Repositories"
type: alert
date: 2026-05-28
source: https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
---
CISA is prioritizing the response to multiple emerging software supply chain intrusion campaigns targeting developer ecosystems Continuous Integration/Continuous Development (CI/CD) pipelines. These recent incidents, including the GitHub compromise via a malicious Nx Console Visual Studio Code (VS Code) extension and the “Megalodon” supply chain intrusion campaign, demonstrate how cyber threat actors are abusing tools and processes that support enterprise, cloud, and DevOps environments—specifically CI/CD pipelines, code extensions and workflows.

Threat actors leveraged a prior compromise of Nx developer systems to compromise a GitHub employee’s device through a poisoned third-party VS Code extension, resulting in unauthorized access and exfiltration of internal GitHub repositories. The malicious extension version (18.95.0) was distributed through VS Code’s automatic update mechanism, meaning systems with Nx Console previously installed may have received the malicious build without developers taking any manual installation action. GitHub released a [security advisory](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w) on this activity, and [CVE-2026-48027](https://www.cve.org/CVERecord?id=CVE-2026-48027) has been assigned to the malicious version of Nx Console and added to [CISA’s Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

Additionally, in a campaign known as “Megalodon,” a cyber threat actor injected malicious GitHub Action workflows to harvest CI/CD secrets, cloud credentials, and tokens, impacting both development and deployment pipelines in public GitHub repositories.

CISA urges organizations to implement the following recommendations to detect and remediate a potential compromise:

*   Monitor and audit workflow files and contributor activity for suspicious pull requests and direct commits, particularly those authored by automated accounts.
*   Revert unauthorized changes, especially from automated accounts, e.g., `build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot` and especially those made after May 18, 2026.

If your organization discovers a compromise resulting from previously compromised GitHub or Nx Console software, CISA recommends the following steps:

*   Conduct a forensics review of CI/CD logs, cloud audit trails, and affected developer machines.
*   Rotate/revoke all secrets including: all credentials, tokens, and secrets accessible to CI/CD pipelines, including API keys, cloud provider credentials (Amazon Web Services, Google Cloud Platform, Microsoft Azure), SSH keys, Docker/npm/PyPI/Vault/Terraform/Kubernetes tokens, GitHub/GitLab/Bitbucket tokens, and developer or pipeline secrets.
*   Notify proper stakeholders if necessary.

CISA recommends the following best practices for using package repos:

*   Wait at least three hours before pulling a new package. This gives the software community time to identify suspicious or malicious packages before they are widely downloaded.
*   Pin software to specific trusted versions. Pinning software prevents pulling a malicious or unscreened package during the build process.
*   Only pull packages from known and trusted sources. Relying on known and trusted sources reduces the likelihood of downloading a package that has been maliciously forked.

See the following resources for additional guidance on these compromises:

*   GitHub: [Investigating unauthorized access to GitHub-owned repositories](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)
*   Nx:[Postmortem: Nx Console v18.95.0 supply-chain compromise](https://nx.dev/blog/nx-console-v18-95-0-postmortem)
*   Ox Security: [Megalodon: CI/CD Malware Spreading Across GitHub Repositories](https://www.ox.security/blog/megalodon-cicd-malware-github/)
*   StepSecurity: [Nx Console VS Code Extension Compromised](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised#indicators-of-compromise)
*   SafeDep: [Megalodon: Mass GitHub Repo Backdooring via CI Workflows](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/)

## **Disclaimer**

The information in this report is being provided “as is” for informational purposes only. CISA does not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document. Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA.
