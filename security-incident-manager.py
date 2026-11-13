#Task 4: Security Incident Manager using Dictionaries

def show_incident(record):
    """Displays every key and its value from a dictionary.
    Parameter: record - the dictionary to display.
    """
    #items() gives each key together with its value
    for key, value in record.items():
        print(f" {key}: {value}")

# Dictionary stores information about a security incident as key-value pairs, and can be updated after it's created.
#Dictionary uses curly brackets {} and stores information as key value pairs
incident = {
    "username": "smith",
    "ip_address": "192.168.1.15",
    "event_type": "Failed login",
    "risk_level": "Medium",
}

#Values are accessed using their keys inside square brackets []
print("Username:", incident["username"])
print("IP address:", incident["ip_address"])

#Added a new field called status
incident["status"] = "Under Investigation"

#Updated the risk level, assigning to an existing key replaces the old value
incident["risk_level"] = "High"

#Removes the key and the value from the dictionary
del incident["event_type"]

#Displays all the remaining keys and values using the show_incident function
print("\nRemaining keys and values:")
show_incident(incident)

#len() counts how many pairs the dictionary holds
print("\nTotal key-value pairs:", len(incident))