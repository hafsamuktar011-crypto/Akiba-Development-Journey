
# parent class
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        #  display logic

    def display_info(self):
      return f"Name: {self.name}, Salary: {self.salary}"

    # create child class with extended name ,salary
class  Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display_info(self):
      return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"    

class  Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language

    def display_info(self):
     return f"Name: {self.name}, Salary: {self.salary}, Programming language: {self.programming_language}"    

manager1=
            
