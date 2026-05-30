x = input("your weight and height is in kg and meter or in inches and pounds? (type k for kg/m or p for pounds/inches):  ")
if x == "k":
    x = int(input("please enter your weight in kg:  "))
    y = float(input("please enter your height in meters:  "))
    z = x / (y ** 2)
    print(f"Your BMI is {z:.2f}")
else:
    x = int(input("please enter your weight in pounds:  "))
    y = float(input("please enter your height in inches:  "))
    z = (x / (y ** 2)) * 703
    print(f"Your BMI is {z:.2f}")

if z < 18.5:
    print("You are underweight.")   
elif 18.5 <= z < 24.9:
    print("You are normal weight.")
elif 25 <= z < 29.9:
    print("You are overweight.")
else:    print("You are obese.")
