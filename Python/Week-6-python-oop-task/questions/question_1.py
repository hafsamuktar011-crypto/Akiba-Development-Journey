
# create class of the obj
class Student:
# initialize student obj 
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department


    def display_info(self):
        print(self.name)
        print(self.student_id)
        print(self.department)

    def introduce(self):
        print("="*50)
        print(f"my name is {self.name} 2nd year of {self.department} and my id is {self.student_id}")    
        print("="*50)

student1=Student("musa","PY-20","python")
student2=Student("musa","CS-20","CS")
student3=Student("musa","IT-20","IT")

for student in (student1,student2,student3):
   student1.display_info()
   student1.introduce()