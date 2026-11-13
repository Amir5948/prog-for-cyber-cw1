# Task 1: Security Tool

# Stored credentials and passwords
USERNAME = "admin"
# The correct username for logging in
PASSWORD = "admin123"
# The correct password for logging in
BRUTE_FORCE_PASSWORD = "Pass1234!"
# The password the user can guess for the brute force

MAX_BRUTE_FORCE_ATTEMPTS = 5
# The maximum number of guesses allowed for brute force
MAX_FAILED_LOGINS = 3
# The number of failed logins allowed before the account is frozen


def authenticate(username, password):
    """Checks whether the username and password are correct.
    The parameters are username and password entered by the user.
    Returns true if both match the stored credentials, otherwise returns false.
    """
    return username == USERNAME and password == PASSWORD
    # Compares both entered values with the stored ones and returns the result


def start_authentication():
    """
    Makes the user log in when the program starts.
    Keeps asking until the correct username and password are entered.
    Takes no parameters and returns nothing.
    """
    while True:
    # Loops forever until the user logs in successfully
        username = input("Enter username: ")
        # Asks the user for their username
        password = input("Enter password: ")
        # Asks the user for their password
        if authenticate(username, password):
        # Checks the details using the authenticate function
            print("Authentication successful.")
            # Tells the user they have logged in
            return
            # Ends the function so the menu can be shown
        print("Authentication failed. Try again.")
        # Runs if the details were wrong, then loops again


def security_event_counter():
    """
    Asks for a password 10 times and counts the correct and incorrect attempts.
    Displays the percentage of incorrect passwords and starts an alert if it is more than 50%.
    """
    correct = 0
    # Counter for the number of correct passwords
    incorrect = 0
    # Counter for the number of incorrect passwords

    for i in range(10):
    # Loops 10 times, once for each password attempt
        guess = input(f"Enter password ({i + 1}/10): ")
        # Asks for a password and shows which attempt it is (i starts at 0)
        if guess == PASSWORD:
        # Checks if the password entered is correct
            correct += 1
            # Adds 1 to the correct counter
        else:
        # Runs if the password entered is wrong
            incorrect += 1
            # Adds 1 to the incorrect counter

    percentage = incorrect / 10 * 100
    # Calculates the percentage of incorrect passwords out of the 10 attempts

    print("Correct passwords:", correct)
    # Displays the number of correct passwords
    print("Incorrect passwords:", incorrect)
    # Displays the number of incorrect passwords
    print(f"Percentage of incorrect passwords: {percentage}%")
    # Displays the percentage of incorrect passwords

    if percentage > 50:
    # Checks if more than 50% of the passwords were incorrect
        print("ALERT: More than 50% of the passwords entered were incorrect!")
        # Raises an alert to warn the user


def brute_force_simulation():
    """
    Simulates a brute-force attack by letting the user guess a password.
    Stops when the correct password is guessed or the max number of attempts is reached.
    """
    attempts = 0
    # Counter for the number of guesses made

    while attempts < MAX_BRUTE_FORCE_ATTEMPTS:
    # Keeps looping while there are attempts left
        guess = input("Enter a password guess: ")
        # Asks the user for a password guess
        attempts += 1
        # Adds 1 to the number of attempts

        if guess == BRUTE_FORCE_PASSWORD:
        # Checks if the guess matches the password
            print(f"Correct password found in {attempts} attempt(s).")
            # Tells the user the password was found and how many attempts it took
            return
            # Ends the function because the password was found

    print("Maximum number of attempts reached. Password not found.")
    # Runs only if the loop ended because all attempts were used up


def login_authentication():
    """
    Asks for a username and password and displays whether authentication accepted or failed.
    Allows three failed logins before showing that the account is frozen for 24 hours.
    """
    failed_logins = 0
    # Counter for the number of failed logins

    while failed_logins < MAX_FAILED_LOGINS:
    # Keeps looping while the user has failed fewer than 3 times
        username = input("Enter username: ")
        # Asks the user for their username
        password = input("Enter password: ")
        # Asks the user for their password

        if authenticate(username, password):
        # Checks the details using the authenticate function
            print("Authentication succeeded.")
            # Tells the user the login worked
            return
            # Ends the function because the login was successful

        failed_logins += 1
        # Adds 1 to the failed logins counter because the details were wrong
        print("Authentication failed.")
        # Tells the user the login failed

    print("Maximum failed logins reached. Your account is frozen for 24 hours.")
    # Runs only if the loop ended because there were 3 failed logins


# Main program
start_authentication()
# The user must log in before the menu is shown

while True:
# Keeps showing the menu until the user chooses Exit
    print("\nSecurity Menu")
    # Displays the menu title (\n adds a blank line before it)
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")
    # Displays the four menu options
    choice = input("Enter your choice: ")
    # Asks the user to pick an option

    if choice == "1":
    # Runs the Security Event Counter if the user enters 1
        security_event_counter()
    elif choice == "2":
    # Runs the Brute-Force Simulation if the user enters 2
        brute_force_simulation()
    elif choice == "3":
    # Runs Login Authentication if the user enters 3
        login_authentication()
    elif choice == "4":
    # Exits the program if the user enters 4
        print("Thank you for using the security tool.")
        # Displays the exit message
        break
        # Stops the menu loop, which ends the program
    else:
    # Runs if the user enters anything other than 1, 2, 3 or 4
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        # Tells the user their choice was invalid, then the menu shows again