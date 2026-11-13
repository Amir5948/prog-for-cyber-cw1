#Task 5: main.py

import security_tools
#Imports the security_tools so its functions can be used in this file

password = input("Enter a password: ")
#Asks the user to enter a password and stores it in password
ip_address = input("Enter an IP address: ")
#Asks the user to enter an IP address and stores it in ip_address

print("\n---Results---")
#Displays a heading for the results (\n adds a blank line before it)

#Check the password
if security_tools.validate_password(password):
#Calls validate_password from the module, which returns true if the password is strong
    print("Password: strong (valid).")
    #Tells the user their password is strong
else:
#Runs if validate_password returned False
    print("Password: weak (invalid).")
    #Tells the user their password is weak
    #Password is not strong so suggest a random strong one
    suggestion = security_tools.generate_password()
    #Calls generate_password from the module and stores the new password in suggestion
    print("Suggested strong password:", suggestion)
    #Displays the suggested strong password

#Check the IP address
if security_tools.validate_ip(ip_address):
#Calls validate_ip from the module, which returns true if the IP address format is valid
    print("IP address:", ip_address, "is valid.")
    #Tells the user the IP address is valid
else:
#Runs if validate_ip returned False
    print("IP address:", ip_address, "is NOT valid.")
    #Tells the user the IP address is not valid