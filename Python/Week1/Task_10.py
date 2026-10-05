# BMI Health Information

name=input("Enter your name ")
weight=float(input("Enter your weight "))
height=float(input("Enter your height "))

height_square=height**2

bmi=weight / height_square
print("================================")
print("          BMI REPORT            ")
print("================================")

print("Name: " ,name)
print("Weight:",weight)
print("Height:" ,height)

print("BMI:", bmi)

print("================================")
