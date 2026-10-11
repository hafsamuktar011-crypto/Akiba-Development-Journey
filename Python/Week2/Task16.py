# FIZZBUZZ

startingNumber = int(input("Please enter the starting number: "))
endingNumber = int(input("Please enter the ending number: "))

# Divisible by both 3 and 5 → FizzBuzz
# Divisible by 3 → Fizz
# Divisible by 5 → Buzz
# Otherwise → print the number

for numbers in range(startingNumber, endingNumber + 1):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FIZZBUZZ")
    elif numbers % 3 == 0:
        print("FIZZ")
    elif numbers % 5 == 0:
        print("BUZZ")
    else:
        print(numbers)