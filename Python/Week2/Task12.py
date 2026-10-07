#  LARGEST OF THREE

number_1=int(input("Enter the first number "))
number_2=int(input("Enter the second number "))
number_3=int(input("Enter the third number "))

if number_1 >= number_2 and number_1 >= number_3:
    print("the largest number is: ",number_1)
elif  number_1 == number_2 and number_3 ==number_1:
    print("All numbers are equal ")
