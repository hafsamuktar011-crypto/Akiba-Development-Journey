 #  Build a program that generates a shopping receipt


# calculate_subtotal(items) — calculate the total cost of all items.
# calculate_discount(subtotal) — apply a discount based on the purchase amount.
# calculate_tax(amount, tax_rate) — calculate tax.
# generate_receipt(items, tax_rate) — return a summary of the purchase.

# Sample Data
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5},
    {"name": "Bag", "price": 1500, "quantity": 2}
]

def calculate_subtotal(items):
    """Calculate the total cost of all items."""
    subtotal = 0

    for item in items:
        if item["price"] < 0:
            raise ValueError(f"Invalid price for {item['name']}. Price cannot be negative.")

        if item["quantity"] < 0:
            raise ValueError(f"Invalid quantity for {item['name']}. Quantity cannot be negative.")

        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    """Apply discount based on subtotal."""
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    """Calculate tax amount."""
    if not (0 <= tax_rate <= 100):
        raise ValueError("Tax rate must be between 0 and 100.")

    return amount * (tax_rate / 100)


def generate_receipt(items, tax_rate):
    """Generate and display the shopping receipt."""
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)

    final_amount = amount_after_discount + tax

    print("\n" + "=" * 40)
    print("         SHOPPING RECEIPT")
    print("=" * 40)

    print(f"{'Product':<15}{'Price':>8}{'Qty':>8}{'Total':>10}")
    print("-" * 40)

    for item in items:
        total = item["price"] * item["quantity"]
        print(
            f"{item['name']:<15}{item['price']:>8.2f}{item['quantity']:>8}{total:>10.2f}"
        )

    print("-" * 40)
    print(f"{'Subtotal:':<30}{subtotal:>10.2f} Birr")
    print(f"{'Discount:':<30}{discount:>10.2f} Birr")
    print(f"{'Tax:':<30}{tax:>10.2f} Birr")
    print(f"{'Final Amount:':<30}{final_amount:>10.2f} Birr")
    print("=" * 40)




tax_rate = 15

generate_receipt(items, tax_rate)

