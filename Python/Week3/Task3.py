# Advanced Number Analyzer

# is_prime(number) — determine whether a number is prime.
# get_divisors(number) — return all positive divisors of a number.
# sum_of_digits(number) — return the sum of its digits.
# reverse_number(number) — return the reversed number.
# analyze_number(number) — return a complete analysis.

number=int(input("enter number: "))
def is_prime(number):
    if number <=1:
        raise ValueError(
            "number can't be less than one"
        )
    for i in range(2,number):
        if number % i  == 0:
            return"not prime"
            
    return "prime"
        
print("the number is :",is_prime(number))

def get_divisors(number):
    # handle negative numbers
    if number == 0 or number < 0:
        raise ValueError("can't be 0")
    divisors=[]

    for i in range(1,number + 1):
        if number % i == 0:              
            divisors.append(i)
    
    return divisors
print(f"the divisor of {number} is :",get_divisors(number))

def sum_of_digits(number):
    # handle negative numbers
    if number < 0:
        number = -number

    total = 0
    while number > 0:
        digit = number % 10   
        total += digit        
        number = number // 10 

    return total

print(f"the sum of {number}is: " ,sum_of_digits(number))
        
def reverse_number(number):
      reverse=[]

      for i in range(number):
          lastDigit=i % 10
          reverse.append(lastDigit)
      return reverse

print(reverse_number(number))       

def analyze_number(number):
    return 