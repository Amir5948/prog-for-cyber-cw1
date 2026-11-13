#Task 5: Reusable Cyber Security Utilities using User-Defined Modules

import random #used to generate random passwords
import string #provides ready-made sets of letters, digits, and symbols

def validate_password(password):
    """Checks whether a password is strong.
    Parameter: password - the password to check.
    Returns True if it is at least 8 characters long and contains at least one letter,
    one digit and one symbol, otherwise returns False.
    """
    #Minimum length check, len() counts the number of characters in the password
    if len(password) < 8:
        #The password is too short, so it is not valid
        return False

    #Starts by assuming the password does not have letters, digits, or symbols
    has_letter = False
    has_digit = False
    has_symbol = False

    #Look at each character and record which types we find
    for char in password:
        #isalpha() returns True if the character is a letter
        if char.isalpha():
            #A letter was found
            has_letter = True
        #isdigit() returns True if the character is a number from 0 to 9
        elif char.isdigit():
            #A digit was found
            has_digit = True
        #string.punctuation contains symbols such as ! @ # $ %
        elif char in string.punctuation:
            #A symbol was found
            has_symbol = True
    #The password is valid only if all 3 types were found
    #"and" means this returns True only when all three are True
    return has_letter and has_digit and has_symbol

def validate_ip(ip_address):
    """Performs a basic format check on an IP address.
    Parameter: ip_address - the IP address to check.
    Returns true if it has 4 numbers separated by 3 dots and each number is between
    0 and 255, otherwise returns falser.
    """
    #Split the address at each dot
    octets = ip_address.split('.')

    #3 dots means exactly 4 parts
    if len(octets) != 4:
        #The wrong number of parts means the format is invalid
        return False
    #Loop through each octet one at a time
    for octet in octets:
        #Each part must only contain digits
        if not octet.isdigit():
            #The octet is not a number, so the IP address is invalid
            return False
        #Convert the octet into an integer
        number = int(octet)
        #Each number must be in the range of 0 to 255
        if number < 0 or number > 255:
            #The number is out of range, so the IP address is invalid
            return False
    #All 4 octets are valid
    return True

def generate_password():
    """ Generates a strong random password.
    Returns a password between 10 and 16 characters long containing at least one capital
    letter, one lowercase letter, one digit and one symbol.
    """
    #Pick a random length between 10 and 16 each time
    length = random.randint(10, 16)
    #Ensure the password has at least one of each type of character
    #random.choice() picks one random character from the group
    password_chars = [
        #One random capital letter
        random.choice(string.ascii_uppercase),
        #One random lowercase letter
        random.choice(string.ascii_lowercase),
        #One random digit
        random.choice(string.digits),
        #One random symbol
        random.choice(string.punctuation),
    ]

    #Fill the remaining length with random characters from all groups
    #all_chars combines letters, digits and symbols into one string
    all_chars = string.ascii_letters + string.digits + string.punctuation
    #Keep adding characters until the password reaches the chosen length
    while len(password_chars) < length:
        #Adds one random character from all groups to the list
        password_chars.append(random.choice(all_chars))

    #Shuffle so that the characters are not always at the start
    random.shuffle(password_chars)
    #Join the list of characters into a single string
    return "".join(password_chars)