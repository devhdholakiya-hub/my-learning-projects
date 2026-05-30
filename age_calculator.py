from datetime import date
y = int(input("Enter Your Birthyear: "))
x = date.today()
if y > 0:
     print(f"Your Birthyear is {y} and Current Year is {x.year}.")
     age = x.year -(y)
     print(f"You are {age} now.")


else:
   print("Invalid Birthyear")   
