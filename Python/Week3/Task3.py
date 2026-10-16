# Advanced Number Analyzer

# is_prime(number) — determine whether a number is prime.
# get_divisors(number) — return all positive divisors of a number.
# sum_of_digits(number) — return the sum of its digits.
# reverse_number(number) — return the reversed number.
# analyze_number(number) — return a complete analysis.

number=int(input("enter number: "))

def is_prime(number):
    if number <= 1:
        return(
            "number can't be less than one"
        )
    for i in range(2,number):
        if number % i  == 0:
            return "not prime"
            
    return "prime"
        
# print("the number is :",is_prime(number))

def get_divisors(number):
    # handle negative numbers
    if number == 0 or number < 0:
        return "divisors are undefined for zero"
    
    divisors=[]

    for i in range(1,number + 1):
        if number % i == 0:              
            divisors.append(i)
    
    return divisors
# print(f"the divisor of {number} is :",get_divisors(number))

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

# print(f"the sum of {number} is: " ,sum_of_digits(number))
        
def reverse_number(number):
      
      reversedNum=0
      while number > 0:
          lastDigit=number % 10       

        # shift the digits and add the last digit
          reversedNum=reversedNum *10 +lastDigit     

      # remove the last digit from the original number
          number=number // 10     

      return reversedNum                      

# print(f"the resversed number of {number} is ",reverse_number(number))       

def analyze_number(number):
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return {
         "number": number,
        "even or odd": parity,
        "prime": is_prime(number),
    
        f"The sum of digits of {number} is": sum_of_digits(number),
        f"The divisors of {number} are": get_divisors(number),
        f"The reversed number of {number} is": reverse_number(number)
    }

print(analyze_number(number))
