# NUMBER ANALYZER
# 
# 
# Problem
# Create a program that asks the user to enter 10 numbers.
# The program should analyze the numbers and display:
# 1. The largest number
# 2. The smallest number
# 3. The total sum
# 4. The average
# 5. How many numbers are even
# 6. How many numbers are odd
# Important
# Try to solve this using one main loop.
# Do not crcreate separate loops for every calculation unless you have a good
# reason.
total = 0
evenNumber = 0
oddNumber = 0

for i in range(10):
    number = int(input("Enter a number: "))

    total += number

    if i == 0:
        largestNumber = number
        smallestNumber = number

    else:
        if number > largestNumber:
            largestNumber = number

        if number < smallestNumber:
            smallestNumber = number

    if number % 2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1

average = total / 10

print("Largest number:", largestNumber)
print("Smallest number:", smallestNumber)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", evenNumber)
print("Odd numbers:", oddNumber)

       
        

