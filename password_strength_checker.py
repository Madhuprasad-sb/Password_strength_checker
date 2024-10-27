import re

def check_password_strength(password):
    # Defining strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        digit_criteria, special_char_criteria])

    # Determine strength level
    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
