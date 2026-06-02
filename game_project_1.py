import random
computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: r=rock, p=paper or s=scissor: ")
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}
you = youDict[youstr]
print(f"you choose {reverseDict[you]} \n and \n computer choose {reverseDict[computer]}")
if you == computer:
    print("it is a tie")

else:
    if (you == 1 and computer == 0):
        print("you win")
    elif (you == 0 and computer == -1):
        print("you win")
    elif (you == -1 and computer == 1):
        print("you win")
    elif (you == 1 and computer == -1):
        print("computer win")
    elif (you == 0 and computer == 1):
        print("computer win")
    elif (you == -1 and computer == 0):
        print("computer win")
    else:
        print("something error!.!.!....")