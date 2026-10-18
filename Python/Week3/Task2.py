# Student Performance Analyzer

# Validate a student's score.
# Calculate a grade.
# Calculate the average score.
# Find the highest and lowest scores.
# Count passed and failed students.
# Generate a report for the class.

# Grade rules:
# Score       Grade
# 90–100         A
# 80–89          B
# 70–79          C
# 60–69          D
# Below 60       F



students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

def getScore(student):
    score = student["score"]
    print(score)

getScore(students[0])

def getGrade(score):
        if score < 60:
            return "F"
        elif score >= 90:
            return "A"
        elif score>=  80 and score <= 89:
            return "B"
        elif score>=  70 and score <= 79:
            return "C"
        elif score>=  60 and score <= 69:
            return "D"
print(f"the score of {37} ",getGrade(37)) 

def calculatAverage(students):
     total=0
     for student in students:
          total += student["score"]
     if len(students) == 0:
          return 0
     else:
          return total/len(students) 
     
calculatAverage(students)

print(calculatAverage(students))

def findHighestScore(students):
     if len(students)==0:
          return None
     
     highest=students[0]["score"]
     for student in students:
          if student["score"] > highest:
               highest=student["score"]
               return highest
print("the highest score",findHighestScore(students))

def findLowestScore(students):
     if len(students)==0:
          return None
     
     lowest=students[0]["score"]
     for student in students:
          if  student["score"] < lowest:
               lowest=student["score"]
               return lowest

print("the lowest score is ",findLowestScore(students))          

def countPassedFailed(students):
     failed=0
     passed=0
     for student in students:
          if student["score"] >= 50:
               passed += 1
               return "pass",passed
          else:
               failed += 1
               return "failed",failed
print(countPassedFailed(students))