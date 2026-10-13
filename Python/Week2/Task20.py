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

Total=0
evenNumber=0
oddNumber=0
for i in range(10):
    number = int(input("Enter a number: "))
    largestNumber=number > i
    smallestNumber=number < i
    print(largestNumber)
