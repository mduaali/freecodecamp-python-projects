# 05_password_generator_project

## Files:
password_generator.py

## What It Does:
This program securely generates random passwords that meet customizable strength requirements.  
It ensures that each password contains at least a specified number of digits, uppercase letters, lowercase letters, and special characters.

## Example:
**Input:**
```python
Code call: generate_password(length=12, nums=2, special_chars=2, uppercase=2, lowercase=2)
Output: Generated password: 4m$T@jR9aZ!p
```

### How It Works:
Uses Python’s secrets module for cryptographically secure random generation.
Uses regular expressions (re.findall) to verify the password meets all character constraints.
Loops until a valid password is generated that satisfies:
Minimum number of digits
Minimum number of special characters
Minimum number of uppercase and lowercase letters

### What I Learned:
How to use secrets.choice() for secure randomization.
How to apply regular expressions to validate patterns in strings.
How to structure constraints using tuples and loops.
How to combine logic and readability with list comprehensions and the all() function.
Why while True loops can safely be used with secure break conditions.
