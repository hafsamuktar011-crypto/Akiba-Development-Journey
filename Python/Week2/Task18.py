# COUNT NUMBERS

Number = int(input("Enter positive number please: "))

# Initialize the variables
n = 1
evenNumber = 0
oddNumber = 0
sumNumbers = 0

while n <= Number:

    if n % 2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1

    sumNumbers += n

    n += 1

# Display the results after the loop finishes
print("Even numbers:", evenNumber)
print("Odd numbers:", oddNumber)
print("Sum of all numbers:", sumNumbers)

            
