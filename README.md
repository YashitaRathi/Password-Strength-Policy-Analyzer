# NIST Password Strength & Policy Analyzer

A Python-based security analysis tool designed to identify weak credential practices
and evaluate organizational password policies against modern security recommendations.

This project focuses on reducing authentication-related risks such as brute-force attacks,
credential stuffing, and poor password enforcement by simulating how security teams assess
password strength and policy compliance.

## Security Use Case

Weak or reused passwords remain one of the most exploited attack vectors in real-world breaches.
This tool demonstrates how defenders can proactively:

• Detect vulnerable password patterns before attackers exploit them  
• Identify high-risk credentials such as dictionary-based or predictable passwords  
• Evaluate whether an organization's password policy aligns with recommended practices  
• Promote passphrase-based authentication as advised by modern standards (e.g., NIST)

## Functional Modules

### 1. Password Risk Analyzer
Evaluates password strength using behavior-based analysis rather than simple complexity rules.

Detects:
- Dictionary / commonly used passwords (blocklist support)
- Sequential characters (e.g., 1234, abc)
- Keyboard walk patterns (e.g., qwerty, asdf)
- Repetitive structures (aaaa, abab)
- Single-character dominance vulnerabilities
- Weak composition disguised as complexity

Supports:
- Passphrase-style passwords (aligned with NIST guidance)
- Context-aware scoring to simulate real risk evaluation

---

### 2. Organizational Policy Auditor
Simulates how security teams review password governance settings.

Analyzes:
- Minimum / maximum length enforcement
- Password expiration policies
- Blocklist usage
- Failed login attempt controls
- Multi-Factor Authentication (MFA) presence
- Passphrase allowance vs forced complexity

Outputs:
- Compliance rating
- Risk score
- Actionable recommendations to strengthen policy

---

## Tech Stack

- Python 3
- Kivy (GUI Framework)
- Custom credential-analysis logic
- NIST-inspired policy evaluation model

## How to Run

1. Install dependencies:
    pip install kivy
2. Run the application:
   python main.py

## Learning Objective

This project was developed to explore defensive security concepts related to:

- Credential hardening
- Authentication risk detection
- Policy enforcement evaluation
- Preventing password-based attack vectors

## Brute-Force Detection Simulation

To extend the learning into authentication monitoring, a simple log-analysis
script was created to detect repeated failed login attempts from the same IP.

This demonstrates how security teams identify potential brute-force attacks
by analyzing authentication logs.

Run:
python bruteforce_detector.py
   
## Author
Yashita Rathi
