NIST_rules = {
    "min_length": {
        "expected": {"min": 8, "max": 64},
        "description": "Minimum password length should be at least 8 characters and maximum 64 characters.",
        "explanation": "Longer passwords are generally more secure as they are harder to guess or brute-force."
    },
    "password_requirement": {
        "expected": False,
        "description": "Passwords should not be required to include specific character types and it should encourage the use of spaces.",
        "explanation": "NIST recommends against forcing users to include specific character types as it can lead to predictable patterns and weaker passwords."
    },
    "password_expiration": {
        "expected": False,
        "description": "Passwords should not have mandatory expiration periods.",
        "explanation": "Frequent password changes can lead to weaker passwords as users may choose simpler passwords or reuse them."
    },
    "password_blocklist": {
        "expected": True,
        "description": "Implement a password blocklist to prevent the use of common or compromised passwords.",
        "explanation": "Blocklists help protect against the use of easily guessable passwords that are often targeted by attackers."
    },
    "no_security_question": {
        "expected": True,
        "description": "Avoid using security questions for account recovery.",
        "explanation": "Security questions can often be guessed or researched by attackers, compromising account security."
    },
    "login_attempts": {
        "expected": 5,
        "description": "Limit the number of failed login attempts to prevent brute-force attacks.",
        "explanation": "Restricting login attempts helps protect accounts from being compromised through repeated guessing."
    },
    "passphrase_support": {
        "expected": True,
        "description": "Passwords should support long passphrases and spaces.",
        "explanation": "Passphrases are easier to remember and harder to guess."
    },
    "mfa_applied": {
        "expected": True,
        "description": "Implement multi-factor authentication to enhance account security.",
        "explanation": "MFA adds an additional layer of security by requiring users to provide multiple forms of verification."
    },
}


def policy_analyzer(policy, NIST_rules):
    score = 0
    issues = []
    suggestions = []
    details = {}

    expected_min = NIST_rules["min_length"]["expected"]["min"]
    expected_max = NIST_rules["min_length"]["expected"]["max"]

    if policy["min_length"] < expected_min:
        issues.append("Minimum length is too low.")
        suggestions.append(
            "Minimum password length should be at least 8 characters.")
        score -= 10
        details["min_length"] = f"Expected greater than or equal to {expected_min}"
    else:
        score += 10

    if policy["max_length"] > expected_max:
        issues.append("Maximum length is too high.")
        suggestions.append(
            "Maximum password length should be 64 only.")
        score -= 5
        details["min_length"] = f"Expected lesser than or equal to {expected_max}"
    else:
        score += 10

    if policy["password_requirement"] != NIST_rules["password_requirement"]["expected"]:
        issues.append("Password Complexitiy rules enabled.")
        suggestions.append(
            "Avoid forcing uppercase/digit/symbol rules. Encourage passphrases instead.")
        score -= 10
        details["password_requirement"] = NIST_rules["password_requirement"]["explanation"]
    else:
        score += 10

    if policy["password_expiration"] != NIST_rules["password_expiration"]["expected"]:
        issues.append("Forced periodic password is enabled.")
        suggestions.append(
            "Disable mandatory resets, they cause weaker passwords.")
        score -= 10
        details["password_expiration"] = NIST_rules["password_expiration"]["explanation"]
    else:
        score += 10

    if policy["password_blocklist"] != NIST_rules["password_blocklist"]["expected"]:
        issues.append("Password blocklist is not enabled")
        suggestions.append(
            "Enable blocklist to prevent common or compromised passwords.")
        score -= 10
        details["password_blocklist"] = NIST_rules["password_blocklist"]["explanation"]
    else:
        score += 10

    if policy["no_security_question"] != NIST_rules["no_security_question"]["expected"]:
        issues.append("Security questions are use for recovery.")
        suggestions.append(
            "Disable security questions — they are easily guessable, instead use multi-factor authentication.")
        score -= 10
        details["no_security_question"] = NIST_rules["no_security_question"]["explanation"]
    else:
        score += 10

    if policy["login_attempts"] > NIST_rules["login_attempts"]["expected"]:
        issues.append("Too many login attempts allowed before lockout.")
        suggestions.append(
            "Reduce allowed failed attempts to 5 to prevent brute-force attacks.")
        score -= 5
        details["login_attempts"] = NIST_rules["login_attempts"]["explanation"]
    else:
        score += 5

    if policy["passphrase_support"] != NIST_rules["passphrase_support"]["expected"]:
        issues.append("Passphrase support is disabled.")
        suggestions.append(
            "Enable passphrases, they are safer and easier to remember.")
        score -= 10
        details["passphrase_support"] = NIST_rules["passphrase_support"]["explanation"]
    else:
        score += 10
    if policy["mfa_applied"] != NIST_rules["mfa_applied"]["expected"]:
        issues.append("MFA is not enforced.")
        suggestions.append(
            "Enable MFA for stronger account security.")
        score -= 10
        details["mfa_applied"] = NIST_rules["mfa_applied"]["explanation"]
    else:
        score += 15

    if score >= 50:
        rating = "Excellent"
    elif score >= 25:
        rating = "Moderate"
    else:
        rating = "Bad"

    return {
        "rating": rating,
        "score": score,
        "issues": issues,
        "suggestions": suggestions,
        "details": details
    }
