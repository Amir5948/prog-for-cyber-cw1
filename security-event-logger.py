# Task 2: Security Event Logger

import random
# Imports the random module, used to create a random Event ID
from datetime import datetime
# Imports datetime, used to get the current date and time for the timestamp

# The correct credentials
CORRECT_USERNAME = "admin"
# The username the user must enter to log in
CORRECT_PASSWORD = "admin123"
# The password the user must enter to log in
IP_ADDRESS = "192.168.1.25"
# The IP address recorded in each event


def create_event(username, event_type):
    """
    Creates a security event record for a login attempt.
    Parameters: username - the username entered by the user,
                event_type - either "Failed login" or "Successsful login".
    Returns a dictionary containing the Event ID, Username, IP Address, Event and Timestamp.
    """
    return {
        "Event ID": random.randint(1000, 9999),
        # Creates a random 4 digit number for the Event ID
        "Username": username,
        # Stores the username that was entered
        "IP Address": IP_ADDRESS,
        # Stores the IP address
        "Event": event_type,
        # Stores whether the login failed or succeeded
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # Stores the current date and time in a readable format:4
    }


event_log = []
# Empty list that will store the event record for every login attempt

while True:
# Keeps asking until the correct username and password are entered
    username = input("Enter username: ")
    # Asks the user for username
    password = input("Enter password: ")
    # Asks the user for password

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
    # Checks if both the username and password are correct
        event_log.append(create_event(username, "Successful login"))
        # Creates a successful login event and adds it to the event log
        break
        # Stops the loop because the correct credentials were entered
    else:
    # Runs if the username or password is wrong
        event_log.append(create_event(username, "Failed login"))
        # Creates a failed login event and adds it to the event log, then the loop asks again

print("\nSecurity event log")
# Displays the title of the event log 
print("---------------------")
# Displays a line under the title

for event in event_log:
# Loops through every event stored in the event log
    print()
    # Prints a blank line to separate each event
    for key, value in event.items():
    # Loops through each field (key) and its value in the event
        print(f"{key}: {value}")
        # Displays the field and its value