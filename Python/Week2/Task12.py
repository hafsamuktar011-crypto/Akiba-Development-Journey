# LARGEST OF THREE

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 == number_2 and number_2 == number_3:
    print("All numbers are equal")

elif number_1 == number_2 and number_2 != number_3:
    print("Number 1 is equal to Number 2")

elif number_2 == number_3 and number_1 != number_2:
    print("Number 2 is equal to Number 3")

elif number_1 == number_3 and number_1 != number_2:
    print("Number 1 is equal to Number 3")

elif number_1 > number_2 and number_1 > number_3:
    print("The largest number is:", number_1)

elif number_2 > number_1 and number_2 > number_3:
    print("The largest number is:", number_2)

else:
    print("The largest number is:", number_3)