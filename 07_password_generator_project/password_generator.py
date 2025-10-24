import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # define constraints as tuples (minimum_required, regex_pattern)
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # check constraints using all() to ensure every rule is satisfied
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    # return the valid password once all conditions are met
    return password

# if this file is run directly, create and display a new password
if __name__ == '__main__':
    new_password = generate_password()
    print('generated password:', new_password)
