import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1

    if re.search(r"[0-9]", password):
        strength += 1

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        strength += 1

    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print(f"Password Strength: {result}")
