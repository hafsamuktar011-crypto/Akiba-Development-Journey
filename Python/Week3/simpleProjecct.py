# Get 5 student scores (input)
# Calculate the average
# Determine pass or fail
# Print the report

def getScores():
    scores=[]
    for i in range(5):
     score=float(input("Enter score: "))

     scores.append(score)
    return scores

print(getScores())
