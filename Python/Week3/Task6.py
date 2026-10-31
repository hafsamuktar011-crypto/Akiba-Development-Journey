# # Inventory Stock Controller
# Create functions to:
# Add a new product.
# Search for a product.
# Update a product's price.
# Increase stock.
# Sell a product.
# Calculate the total inventory value.
# Generate a low-stock report.

inventory = {}

def addProduct(name,price,stock):
    if name == "":
        print("Error: Product name cannot be empty.")
        return
    if name in inventory:
        print("Error: Product already exists.")
        return