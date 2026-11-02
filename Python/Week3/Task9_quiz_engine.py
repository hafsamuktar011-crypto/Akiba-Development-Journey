# Reusable Quiz Engine

# Build a command-line quiz program using functions.
# Each question should contain a question, a list of options, and the correct answer.
# Create functions to:
# Display a question.
# Validate an answer.
# Check whether the answer is correct.
# Update the score.
# Display the final results.

# it holds the question, options,and correct answer
def displayQueston(questionData):
    # iterate the array of one dictionary
    for questions in questionData:
      print(questions["question"])
      print("options:")
    #   iterate option belongs to iterated upper question
      for option in questions["options"]:
        print(option)
        print("-"*40)

# check the ans is belongs to option or not
def validateAnswer(useranswer,questiondata):
    
    for questions in questionData:
       if useranswer == questions:
          return True
       return False
       


# def correctAnswer(questionData):
           

questionData = [
    {
    "question": "What is the capital of Ethiopia?",
    "options": ["A. Addis Ababa", "B. Nairobi", "C. Cairo", "D. Kampala"],
    "correct_answer": "A"
},
 {
    "question": "What is 2 + 2?",
    "options": ["A.33", "B.4", "C.43", "D.23"],
    "correct_answer": "B"
},
  {
        "question": "Which language is used for web development?",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "D"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "A"
    }

]

displayQueston(questionData)
print(validateAnswer("r","Which data type stores True or False?"))