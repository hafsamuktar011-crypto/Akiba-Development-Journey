
# parent class
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        #  display logic
    def display_info(self):
        return "display"
    # create child class with extended name ,salary
class  Manager:
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

class  Developer:
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
            
