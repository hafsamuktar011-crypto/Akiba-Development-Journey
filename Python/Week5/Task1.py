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
        # display method
    def display_info(self):
        print(f"Name: {self.name}")    
        print(f"Age: {self.age}")    
        print(f"Department: {self.department}")

#  student obj creation           
student1=Student("Moxammed","22","computer science") 
student2=Student("Axmed","28","computer science") 
student3=Student("Fatum","38","Electrical engineering") 

        # display info of 3 student
student1.display_info()        
student2.display_info()        
student3.display_info()        