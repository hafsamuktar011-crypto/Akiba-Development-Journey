# SUM OF DIGITS

num = 234

# Initialize sum of digits
total = 0

while num > 0:
    lastD = num % 10
    total += lastD
    num = num // 10

print(total)