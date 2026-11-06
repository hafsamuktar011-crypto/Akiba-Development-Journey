from abc import ABC,abstractclassmethod
# part A
# polymerphism 

class Dog:
    def  make_sound(self):
        print(f"the sount of dog is woof")
class Cat:
    def  make_sound(self):
        print(f"the sount of cat is meow")
class Cow:
    def  make_sound(self):
            print(f"the sount of cow is bbooww")
    
dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound() 

# part b

class Shape(ABC):
     @abstractclassmethod
     def calculate_area(self,lenght,width,):
         pass
class Rectangle:
     def calculate_area(self):
          self.length=self.length
          self.length=self.length
          
     

class Circle:
          
     

  