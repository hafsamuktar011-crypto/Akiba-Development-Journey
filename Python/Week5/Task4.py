# Product Information System
# Create a Product class with the following requirements:
# Define attributes: name, price, and quantity.
# Use __init__() to initialize the attributes.
# Implement __str__() to return a readable description of a product.
# Create at least three product objects.
# Print each object directly using print().
# Add a method called total_value() that calculates the total value using price × quantity.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"The description of the product name:{self.name} quantity:{self.quantity} price:{self.price}"
    # create product obj
product1=Product("Brake pads",)    
product1=Product("Shock absorber",)    
product1=Product("Radiator",)    