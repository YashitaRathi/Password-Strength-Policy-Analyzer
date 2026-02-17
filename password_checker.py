COMMON_PASSWORD = set()


def checkPassword(pasw, personal_info=None):
    points = 0
    issues = []
    suggestions = []
    details = {}
    basic_result = basic_check(pasw)
    details['basic_check'] = basic_result

    if basic_result['points'] < 4:
        issues.append("Password does not meet basic complexity requirements.")
        suggestions.append(
            "Ensure your password is at least 8 characters long and includes uppercase letters, lowercase letters, digits, and special characters.")
        points -= 4
    else:
        points += 5

    if weak_passwords(pasw):
        issues.append("Password is too common.")
        suggestions.append(
            "Avoid using common passwords. Choose a more unique password.")
        details['weak_passwords'] = True
        points -= 5
    else:
        points += 2

    rep = repeat_char(pasw)
    details['repeat_char'] = rep
    if rep['repetitive']:
        issues.append("Password contains repetitive patterns.")
        suggestions.append(
            "Avoid using repetitive characters or sequences in your password. eg. abab, aaaaa")
        points -= 2
    else:
        points += 1

    seq = sequential_num(pasw)
    details['sequential_num'] = seq
    if seq['sequential']:
        issues.append("Password contains sequential numbers.")
        suggestions.append(
            "Avoid using sequential numbers in your password. eg. 1234, 9876")
        points -= 2
    else:
        points += 1

    alp = alpabetical_seq(pasw)
    details['alpabetical_seq'] = alp
    if alp['sequential']:
        issues.append("Password contains sequential alphabets.")
        suggestions.append(
            "Avoid using sequential alphabets in your password. eg. abcde, pqrs")
        points -= 2
    else:
        points += 1

    key = keyboard_patterns(pasw)
    details['keyboard_patterns'] = key
    if key['keyboard']:
        issues.append("Password contains keyboard patterns.")
        suggestions.append(
            "Avoid using keyboard patterns in your password. eg. qwert, asdf")
        points -= 2
    else:
        points += 1

    passphrase = passphrase_check(pasw)
    if passphrase['ispassphrase']:
        points += passphrase['points']
        suggestions.append(passphrase['description'])
        details['passphare'] = True
    else:
        details['passphare'] = False
        suggestions.append(passphrase['suggestion'])

    if personal_info:
        password_lower = pasw.lower()
        matched_items = []

        for key, value in personal_info.items():
            if value and value.lower() in password_lower:
                matched_items.append((key, value))

        if matched_items:
            issues.append(
                f"Password contains personal information: {', '.join(v for k, v in matched_items)}.")
            suggestions.append(
                "Avoid using names, birth years, pet names, or other personal details in your password."
            )
            details['personal_info'] = {
                "matched": True,
                "items": [v for k, v in matched_items]
            }
            points -= 4
        else:
            details['personal_info'] = {
                "matched": False
            }
            points += 2

    if points <= 0:
        points = 0
    strength = ""
    if points <= 3:
        strength = "Very Weak"
    elif points <= 6:
        strength = "Weak"
    elif points <= 9:
        strength = "Moderate"
    elif points >= 10:
        strength = "Strong"
    return {
        "strength": strength,
        "points": points,
        "issues": issues,
        "suggestions": suggestions,
        "details": details
    }


def load_common_passwords(filepath):
    global COMMON_PASSWORD
    try:
        with open(filepath, 'r') as file:
            COMMON_PASSWORD = {line.strip().lower()
                               for line in file if line.strip()}
            print(f"Loaded {len(COMMON_PASSWORD)} common passwords.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        COMMON_PASSWORD = set()
    except Exception as e:
        print(f"An error occurred: {e}")
        COMMON_PASSWORD = set()


load_common_passwords("common_password.txt")


def weak_passwords(searchpassword):
    if searchpassword.lower().strip() in COMMON_PASSWORD:
        return True
    else:
        return False


def basic_check(passw):
    points = 0
    length = len(passw) >= 8
    is_upper = any(char.isupper() for char in passw)
    is_lower = any(char.islower() for char in passw)
    is_digit = any(char.isdigit() for char in passw)
    is_special = any(
        char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?` ~" for char in passw)
    if length:
        points += 1
    if is_upper:
        points += 1
    if is_lower:
        points += 1
    if is_digit:
        points += 1
    if is_special:
        points += 1
    return {
        "points": points,
        "length": length,
        "is_upper": is_upper,
        "is_lower": is_lower,
        "is_digit": is_digit,
        "is_special": is_special
    }


def repeat_char(passw):
    pasw = passw.lower()
    result = same_char(pasw)
    if result['repetitive']:
        return result
    result = single_char(pasw)
    if result['repetitive']:
        return result
    result = repeating_pattern(pasw, 2)
    if result['repetitive']:
        return result
    result = repeating_pattern(pasw, 3)
    if result['repetitive']:
        return result
    result = repeating_pattern(pasw, 4)
    if result['repetitive']:
        return result
    return {'repetitive': False}


def same_char(pasw):
    current_char_count = 1
    max_repeats = 1
    for i in range(1, len(pasw)):
        if pasw[i] == pasw[i-1]:
            current_char_count += 1
            max_repeats = max(max_repeats, current_char_count)
        else:
            current_char_count = 1
    if max_repeats >= 4:
        return {
            'repetitive': True,
            'type': 'consecutive same-character runs',
            'details': f'Maximum consecutive same-character run length: {max_repeats}'
        }
    return {
        'repetitive': False
    }


def single_char(pasw):
    freq = {}
    for char in pasw:
        freq[char] = freq.get(char, 0) + 1
    max_count = max(freq.values())
    ratio = max_count / len(pasw)
    if ratio >= 0.4 and len(pasw) >= 5:
        return {
            'repetitive': True,
            'type': 'single-character dominance',
            'details': f'Character "{max(freq, key=freq.get)}" appears {max_count} times ({ratio:.2%} of password)'
        }
    else:
        return {
            'repetitive': False
        }


def repeating_pattern(passw, p_len):
    pasw = passw.lower()
    if len(pasw) >= p_len and len(pasw) % p_len == 0:
        pattern = pasw[0:p_len]
        repeat = len(pasw)//p_len

        if pattern * repeat == pasw:
            return {
                'repetitive': True,
                'type': f'{p_len} character-repeating',
                'details': f'Repeating pattern: {pattern}'
            }
        else:
            return {
                'repetitive': False
            }
    return {
        'repetitive': False
    }


def check_sequence(passw, min_length):
    if len(passw) < min_length:
        return {
            'sequential': False
        }
    asc, des, max_seq = 1, 1, 1
    for i in range(1, len(passw)):
        prev_val = ord(passw[i-1]) if not passw[i -
                                                1].isdigit() else int(passw[i-1])
        cur_val = ord(passw[i]) if not passw[i].isdigit() else int(passw[i])
        if cur_val == prev_val + 1:
            asc += 1
            des = 1
        elif cur_val == prev_val - 1:
            asc = 1
            des += 1
        else:
            asc = 1
            des = 1
        max_seq = max(max_seq, asc, des)
    if max_seq >= min_length:
        return {
            'sequential': True,
            'type': 'sequential digits',
            'details': f'Maximum sequential digit length: {max_seq}'
        }
    return {
        'sequential': False
    }


def sequential_num(passw):
    digit_only = "".join(char for char in passw if char.isdigit())
    result = check_sequence(digit_only, 3)
    if result['sequential']:
        result['type'] = 'sequential digits'
        return result
    return {'sequential': False}


def alpabetical_seq(passw):
    alpha_only = "".join(char for char in passw if char.isalpha()).lower()
    result = check_sequence(alpha_only, 3)
    if result['sequential']:
        return {
            'sequential': True,
            'type': 'sequential alphabets',
            'details': result['details']
        }
    else:
        return {
            'sequential': False
        }


def keyboard_patterns(passw):
    keyboard_rows = [
        "qwertyuiop", "asdfghjkl", "zxcvbnm", "123456789-=", "!@#$%^&*()_+"
    ]
    if len(passw) >= 4:
        pasw = passw.lower()
        for row in keyboard_rows:
            for i in range(len(row) - 3):
                pattern = row[i:i+4]
                rev_pattern = pattern[::-1]
                if pattern in pasw or rev_pattern in pasw:
                    return {
                        'keyboard': True,
                        'type': 'keyboard pattern',
                        'details': f'Pattern found: {pattern} or {rev_pattern}'
                    }
        return {
            'keyboard': False
        }
    return {
        'keyboard': False
    }


def passphrase_check(pasw):
    if len(pasw) >= 12 and " " in pasw:
        return {
            'ispassphrase': True,
            'points': 5,
            'description': "Excellent! You are using a passphrase, which is highly recommended by NIST."
        }
    return {
        'ispassphrase': False,
        'suggestion': 'Consider using a passphrase, as recommended by NIST.',
        'points': 0
    }
