# Task 1: Student Information System

# Create a Student class with the following requirements:
# Define attributes: name, age, and department.
# Use __init__() to initialize the attributes.
# Create a display_info() method to display the student's information.
# Create three student objects with different information.
# Display the information of all three students.

class Student:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
    def display_info(self):
        print(f"Name: {self.name}")    
        print(f"Age: {self.age}")    
        print(f"Department: {self.department}")
            
        