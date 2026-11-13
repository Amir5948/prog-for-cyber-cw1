#Task 3: IP Address Validator

def validate_ip(ip):
    """Checks whether an IP address has a valid format.
    Takes the IP address as a parameter
    Returns true if the IP address meets the requirements, otherwise returns false."""

    ip = ip.strip()
    #Removes any spaces from the start and end of the IP address

    if "." not in ip:
    #Checks if there are no dots in the IP address
        return False
        #Stops the function and returns false because there are no dots

    if ip.count(".") != 3:
    #Counts the dots and checks if there are not exactly 3
        return False
        #Stops the function and returns false because there are not exactly 3 dots

    parts = ip.split(".")
    #Splits the IP address at each dot into a list

    if len(parts) != 4:
    #Checks if the list does not have exactly 4 parts
        return False
        #Stops the function and returns False because there are not 4 parts

    for part in parts:
    #Loops through each part of the IP address

        if not part.isdigit():
        #Checks if the part contains anything that is not a digit
            return False
            #Stops the function and returns false because the part is not a number

        number = int(part)
        #Converts the part from a string (text) into an integer

        if number < 0 or number > 255:
        #Checks if the number is less than 0 or more than 255
            return False
            #Stops the function and returns false because the number is less than 0 or more than 255

    return True
    #If every check has passed, returnstrue because the IP address is valid


ip_address = input("Enter an IP address: ")
#Asks the user to enter an IP address and stores it in ip_address

if validate_ip(ip_address):
#Calls the validate_ip function with the user's IP address and checks if it returned true
    print("Valid IP address")
    #Prints this message if the IP address is valid
else:
#Runs if the function returned False
    print("Invalid IP address")
    #Prints this message if the IP address is invalid