# shopping reciept
custoer_name=input("Enter your name please ")
product_name=input("Enter your product name please ")
price=int(input("Enter price please "))
quantity=int(input("Enter the product quantity please "))

totalPrice=float(price * quantity)

print("==================================" )
print("             RECEIPT   ") 
print("==================================")
print("customer: ", custoer_name)

print(f"{'Product':<15}    {'Price':>10}  {'Qty':>5}")
print("-----------------------------------")

print(f"{product_name:<15} {price:>10} {quantity:>5}")
 
print("Total",totalPrice)
print("Thank you for shopping!")
print("========================")
