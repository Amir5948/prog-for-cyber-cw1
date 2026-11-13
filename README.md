# Cyber Security Utilities

# Student Details
Amir Afzal
New College Lanarkshire (Motherwell)
B01888688

# What the Program Does
This program is a small collection of reusable cyber security functions organised into a separate mdoule.

# Files
- security_tools.py – the module containing three reusable functions:
  - `validate_password()` – checks that a password is at least 8 characters long and contains at least one letter, one digit and one symbol
  - `validate_ip()` – performs a basic format check on an IP address (three dots, 4 numbers, each between 0 and 255)
  - `generate_password()` – generates a strong random password between 10 and 16 characters long, with a random length each time, containing capital letters, lowercase letters, digits and symbols
- **main.py** – imports `security_tools`, asks the user for a password and an IP address, and displays whether each one is valid. If the password is not strong, it suggests a randomly generated strong password.

# How to Run
1. Make sure `security_tools.py` and `main.py` are in the same folder.
2. Open a terminal in this folder.
3. Run:
   python main.py
5. Enter a password and an IP address when asked.