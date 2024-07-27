import random

rounds = 3 
score = 0
options = ["rock", "paper","scissors"]
computer_option = random.choice(options)
user_option = str(input("Rock , Paper , Scissors: ")).lower()
if user_option not in options:
    print("choose a valid option")


def point_system(user_option , computer_option):
    global score
    global rounds
    if user_option == computer_option:
        print(f" You both picked {computer_option}  therfore it is a draw")
        print("you did not gain any point , bc you both picked the same option")
        rounds = rounds - 1 
    elif user_option == "rock" and computer_option == "scissors":
        ("print you won bc the computer picked scissors")
        score += 1
        rounds = rounds - 1 
    elif user_option == "scissors" and computer_option == "paper":
        print("you won , you gain a point bc the computer picked paper")
        score += 1
        rounds = rounds - 1 
    elif user_option == "paper" and computer_option == "rock":
        print("you won , you gain a point bc the computer picked rock")
        score += 1
        rounds = rounds - 1 
    else:
        print("you lost")
        score = score + 1
        rounds = rounds - 1 


    
point_system(user_option , computer_option)
