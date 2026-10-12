# ATM PIN SYSTEM

# Problem
# Create a simple ATM PIN verification program.
# The correct PIN is:
# 1234
# The user gets a maximum of 3 attempts to enter the correct PIN.
# Requirements
# Use:
# while or another appropriate loop
# Conditions
# Counter
# User input
# Challenge
# Display how many attempts remain.
# Example:
# Incorrect PIN.
# Attempts remaining: 2

pin=int(input("Enter the correct PIN "))
attempt=0

correctPin=1234
while attempt <= 3:
    attempt +=1
    if pin == correctPin:
        alert=input("congrats you have entered correct pin !!")
    if pin != correctPin:
     alert=int(input("Attempts remaining  2 "))
    if pin != correctPin: 
          alert=int(input("Attempts remaining 1 "))
    else:
          alert=int(input("Attempts finished "))
    break
