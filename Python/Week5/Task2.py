# Rectangle Calculator
# Create a Rectangle class with the following requirements:
# Initialize length and width using __init__().
# Create an area() method to calculate the area.
# Create a perimeter() method to calculate the perimeter.
# Create two rectangle objects with different dimensions.
# Display the area and perimeter of each rectangle.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length *self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
    def __str__(self):
         return f"Rectangle(length={self.length}, width={self.width})"

# create two rectangle obj
rectangle1=Rectangle(4,2)
rectangle2=Rectangle(8,3)

# display rectangle dimension
print(rectangle1)
print(rectangle2)

# display area and perimeter
print(f"AREA of rectangle 1:",rectangle1.area())

print(f"Perimeter of rectangle 1:",rectangle1.perimeter())

print(f"AREA of rectangle 2:",rectangle2.area())
print(f"Perimeter of rectangle 2:",rectangle2.perimeter())
