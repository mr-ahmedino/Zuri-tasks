import random
user = input("Pick your choice from Rock(R),Paper(P) and Scissors(S):")
if user != ["R", "P", "S"]:
    print("Your answer is Invalid,pick between 'R','P' and 'S'")
options = ["R", "P", "S"]
computer = random.choice(options)
print("You picked", user,"Computer picked",computer)
if user == computer:
    print("Both users picked the same value,it's a tie")
elif user == "R":
    if computer == "S":
        print("Rock wins paper by smashing!")
    else:
         print("Paper covers rock,you lose!")
elif user == "P":
    if computer == "R":
        print("Paper covers rock,You won!")
    else:
        print("Scissors cut paper,You lose")
elif user == "S":
    if computer == "P":
        print("Scissors cuts paper,You win!")
    else:
        print("Rock smashes scissors,you lose!")
