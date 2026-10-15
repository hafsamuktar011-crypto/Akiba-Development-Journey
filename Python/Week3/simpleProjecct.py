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



def calculateAverage(scores):
   sumofScore=0
   for i in scores:
      sumofScore+=i
      return sumofScore/len(scores)

scores=getScores()
print("scores: ",scores)

print(calculateAverage(scores))
