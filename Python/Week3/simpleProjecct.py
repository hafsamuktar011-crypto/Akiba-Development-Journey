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
def checkPassFail(average):
   if average >= 5:
    return "pass"   
   else:
      return "fail"

def print_report(scores, average, result):
    print("\nReport")
    print("Scores:", scores)
    print("Average:", average)
    print("Result:", result)

scores=getScores()
average=calculateAverage(scores)
result=checkPassFail(average)

print("scores: ",scores)

print(average)
print(result)
print(scores,average,result)
