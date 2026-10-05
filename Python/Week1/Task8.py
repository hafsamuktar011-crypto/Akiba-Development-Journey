name=input("Enter your name ")
python_score=int(input("Enter your python score "))
english_score=int(input("Enter your english score "))
mathematics_score=int(input("Enter your mathematic score "))

sumOfScore=python_score + english_score + mathematics_score

average=float(sumOfScore / 3)


print("========================================")
print("              STUDENT RESULT           ")
print("========================================")

print("Student:" ,name)

print("Python:" ,python_score)
print("English:" ,english_score)
print("Mathematics:" ,mathematics_score)

print("---------------------------------")


print("Average",average)

print("==========================================")