# Zero Trust Network Access Simulation
# Project: ZTNA using Zscaler

import datetime

# User database
users = {
    "admin": "admin123",
    "employee": "emp123",
    "student": "stu123"
}

# Trusted devices
trusted_devices = ["laptop", "desktop"]

# Allowed locations
allowed_locations = ["office", "campus", "vpn"]

# Function to log activity
def log_activity(user, status):
    time = datetime.datetime.now()
    file = open("ztna_log.txt", "a")
    file.write(user + " - " + status + " - " + str(time) + "\n")
    file.close()

# Login function
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful")
        return username
    else:
        print("Login Failed")
        return None

# Device verification
def verify_device():
    device = input("Enter Device Type (laptop/desktop/mobile): ")

    if device in trusted_devices:
        print("Device Verified")
        return True
    else:
        print("Untrusted Device")
        return False

# Location verification
def verify_location():
    location = input("Enter Location (office/campus/vpn/home): ")

    if location in allowed_locations:
        print("Location Verified")
        return True
    else:
        print("Unauthorized Location")
        return False

# Main program
print("===================================")
print(" Zero Trust Network Access System ")
print("===================================")

user = login()

if user:
    device_status = verify_device()
    location_status = verify_location()

    if device_status and location_status:
        print("Access Granted")
        log_activity(user, "Access Granted")
    else:
        print("Access Denied")
        log_activity(user, "Access Denied")
else:
    print("Authentication Failed")