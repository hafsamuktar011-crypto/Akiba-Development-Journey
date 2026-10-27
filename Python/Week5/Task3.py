# # Task 3: Student Score Management
# Create a Student class with the following requirements:
# Define a class attribute school_name = "Akiba Academy".
# Define instance attributes name, score, and department.
# Create a display() method to display all student information.
# Create at least three student objects.
# Update the score of one student and display the updated information.
# Demonstrate that each student has an independent score.

class Student:
    school_name = "Akiba Academy"
    def __init__(self,name,school,department):
        self.name=name
        self.school=school
        self.department=department
    def display(self):
        return print("school:",self.school_name)
                    ("name:",self.name)
student1=    
