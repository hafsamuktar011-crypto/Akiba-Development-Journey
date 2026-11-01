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
    print(questionData["question"])
    # iterate the array of option
    for option in questionData["options"]:
        print(option)



questionData = {
    "question": "What is the capital of Ethiopia?",
    "options": ["A. Addis Ababa", "B. Nairobi", "C. Cairo", "D. Kampala"],
    "correct_answer": "A"
}
displayQueston(questionData)