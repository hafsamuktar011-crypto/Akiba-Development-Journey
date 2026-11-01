# Password Policy and Strength Analyzer

# Create a function-based password validation system.
# Create functions to check:
# Minimum length.
# Uppercase letters.
# Lowercase letters.
# Digits.
# Special characters.

password=""
# password="1234456"

# default mininum length =8

def minimumlength(password,minLength=8):
     if len(password) >= minLength:
      return True
     return False

    # def hasUppercaseCase(password):   
    # def hasLowercaseCase(password):
    #    def hasDigits(password):  
    #       def hasSpecialCharacter(password): 

# analyzepassword return the all of the result of the functions
def analyzePassword(password):
        result=  {"minium length":minimumlength(password)}   

        return result   
print(analyzePassword("hello123"))   
print(analyzePassword("hello@1233"))   
print(analyzePassword("hel3"))   