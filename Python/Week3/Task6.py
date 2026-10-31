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

def add_product(name,price,stock):
    if name == "":
        print("Error: Product name cannot be empty.")
        return
    if name in inventory:
        print("Error: Product already exists.")
        return
    if price < 0:
        print("Error: Price cannot be negative.")
        return

    if stock < 0:
        print("Error: Stock cannot be negative.")
        return
    inventory[name] = {
        "price": price,
        "stock": stock
    }
    print(name, "added successfully.")


def search_product(name):
    if name in inventory:
        return inventory[name]

    return "Product not found."


def update_price(name, new_price):
    if name not in inventory:
        print("Product not found.")
        return

    if new_price < 0:
        print("Error: Price cannot be negative.")
        return

    inventory[name]["price"] = new_price
    print("Price updated successfully.")


def increase_stock(name, quantity):
    if name not in inventory:
        print("Product not found.")
        return

    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return

    inventory[name]["stock"] += quantity
    print("Stock increased successfully.")


def sell_product(name, quantity):
    if name not in inventory:
        print("Product not found.")
        return

    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return

    if quantity > inventory[name]["stock"]:
        print("Error: Not enough stock available.")
        return

    inventory[name]["stock"] -= quantity
    print("Sale completed successfully.")


def total_inventory_value():
    total = 0

    for product in inventory:
        total = total + (
            inventory[product]["price"]
            * inventory[product]["stock"]
        )

    return total


def low_stock_report(threshold):
    print("Low Stock Products:")

    for product in inventory:
        if inventory[product]["stock"] < threshold:
            print(
                product,
                "- Stock:",
                inventory[product]["stock"]
            )


# Example
add_product("Laptop", 1200, 10)
add_product("Mouse", 25, 3)
add_product("Keyboard", 50, 4)

print(search_product("Mouse"))

update_price("Mouse", 30)

increase_stock("Mouse", 2)

sell_product("Laptop", 2)

print("Total Inventory Value:", total_inventory_value())

low_stock_report(5)