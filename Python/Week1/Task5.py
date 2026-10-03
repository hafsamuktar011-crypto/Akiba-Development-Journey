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
print("Product   ,     Price       ,  Qty")
print("-----------------------------------")
print(product_name ,   price,   quantity)
print("Total",totalPrice)
print("Thank you for shopping!")
print("========================")
