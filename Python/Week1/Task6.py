
employee_name=input("Enter employee name ")
salary=int(input("Enter salary "))
transport_allowance=int(input("enter transport allowance "))
food_allowance=int(input("enter food allowance "))

gross_salary = salary  + transport_allowance + food_allowance

print("===================================")
print("         EMPLOYEE PAYSLIP          ")
print("===================================")

print("Employee: ",employee_name ,"ETB")
print("Basic Salary:" ,salary ,"ETB")
print("Transport Allowance:",transport_allowance ,"ETB")
print("Food Allowance:" ,food_allowance ,"ETB")

print("----------------------------------")
print("Gross Salary", gross_salary, "ETB")

print("====================================")
