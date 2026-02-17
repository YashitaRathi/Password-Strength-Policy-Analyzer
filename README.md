# NIST Password Strength & Policy Analyzer

A desktop application built using Python and Kivy that:
  - Evaluates password strength based on NIST guidelines
  - Detects common attack patterns
  - Analyzes organizational password policies for compliance

## Features

### Password Strength Analyzer
- Checks minimum length and character diversity
- Detects common passwords (blocklist support)
- Identifies:
  - Sequential characters (1234, abc)
  - Keyboard patterns (qwerty, asdf)
  - Repetitive characters (aaaa, abab)
  - Single-character dominance
- Passphrase detection (NIST-recommended)
- Context-based scoring system

---

### Organization Policy Analyzer
- Evaluates password policy settings against NIST recommendations
- Checks:
  - Minimum and maximum length rules
  - Password expiration policies
  - Blocklist enforcement
  - Login attempt limits
  - MFA implementation
  - Passphrase support
- Provides:
  - Compliance rating
  - Numerical score
  - Improvement suggestions

---

## 🛠 Tech Stack

- Python 3
- Kivy (GUI Framework)
- Custom security algorithms
- NIST-based policy evaluation logic

## How to Run

1. Install dependencies:
    pip install kivy
2. Run the application:
   python main.py
   
## Author
Yashita Rathi
