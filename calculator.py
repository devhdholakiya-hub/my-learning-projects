x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = input("Enter the operator: ") 
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
else:    print("Invalid operator")