# Security Event Logger

# Student Details
Amir Afzal
New College Lanarkshire (Motherwell)
B01888688

# What the Program Does
This program records security events for login attempts. It keeps asking the user for a username and password until the correct details are entered.

Every login attempt, failed or successful, is recorded as  containing:
- Event ID – a random 4 digit number
- Username – the username entered
- IP Address – the IP address of the system
- Event – "Failed login" or "Successful login"
- Timestamp – the date and time of the attempt

Once the user logs in successfully, the program prints the event log for every attempt.

# How to Run
1. Open a terminal in this folder.
2. Run:
   python security_event_logger.py
3. Enter a username and password when asked.