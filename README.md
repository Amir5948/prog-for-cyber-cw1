# IP Address Validator

# Student Details
Amir Afzal
New college Lanarkshire (Motherwell)
B01888688

# What the Program Does
This program asks the user to enter an IP address and checks whether it has a basic valid IPv4 format using a function called `validate_ip()`.

The function:
- Takes the IP address as a parameter
- Removes spaces from the start and end of the input
- Checks the IP address contains dots
- Checks there are exactly three dots
- Checks there are four numbers
- Checks each number is between 0 and 255
- Returns True if all checks pass, otherwise returns False

The program then displays "Valid IP address" or "Invalid IP address".

# How to Run
1. Open a terminal in this folder.
2. Run:
   python ip_address_validator.py
3. Enter an IP address when asked.
