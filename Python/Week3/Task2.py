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


def getScore(students):
    for student in students:
        score = student["score"]
        print(score)

getScore(students)
