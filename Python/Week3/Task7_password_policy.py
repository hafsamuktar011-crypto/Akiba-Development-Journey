# Password Policy and Strength Analyzer

# Create a function-based password validation system.
# Create functions to check:
# Minimum length.
# Uppercase letters.
# Lowercase letters.
# Digits.
# Special characters.




# default mininum length =8

def minimumlength(password,minLength=8):
     if len(password) >= minLength:
      return True
     return False

def hasUppercaseCase(password):
    for char in password:
        if char.isupper():
            return True
    return False
   
def hasLowercaseCase(password):
     for char in password:
      if char.islower():
          return True
     return False

def hasDigits(password):
     for char in password: 
      if char.isdigit():
          return True
     return False  

# check char is a letter or number
def hasSpecialCharacter(password):
     for char in password:
      if not  char.isalnum():
          return True
     return False 

# analyzepassword return the all of the result of the functions
def analyzePassword(password):
        
        results=  {"minium length":minimumlength(password),
                  "uppercase":hasUppercaseCase(password),
                  "lowercase ":hasLowercaseCase(password),
                  "digit":hasDigits(password),
                  "special character":hasSpecialCharacter(password)
                  } 
          
        missing=[]
        # gets dictionary key value
        for key,value in results.items():
            if value is False:
                missing.append(key)
        return{
                    "results":results,
                    "missing requirements":missing
                }
           

print(analyzePassword("hello123"))   
print(analyzePassword("hello@1233"))   
print(analyzePassword("WERTTYY"))   
print(analyzePassword("weQ234$21"))   
print(analyzePassword("Helo23!@0r"))   