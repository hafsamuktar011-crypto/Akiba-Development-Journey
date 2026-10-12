# ATM PIN SYSTEM

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
