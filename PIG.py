import random
score = 0

def condition_for_roll(roll):
    global score
    if roll == 1:
        print("you lost")
        print(score)
        
approval = input("Do you want to play the PIG game (yes) or (no): ").lower()
while approval == "yes" :
    try:
        players = int(input("how many players  do you want  to play with? (2-4) "))
        if 2 <= players and 4 >= players:
            break
        else:
            print("the number of players should be between 2-4 ")
    except TypeError:
        print("please enter a valid input")

else:
    print("good bye")
    quit()

score_of_players = [0 for i in range(players)]

status = str(input("Do you want to roll (yes) or (no)")).lower()
while status == "yes":
    roll = random.randint(1,6)
    condition_for_roll(roll)
    print(f"you rolled a dice with {roll} points")
    score += roll
    roll = random.randint(1,6)
    condition_for_roll(roll)
    
    status = str(input("Do you continue rolling (yes) or (no)")).lower()
    
        
else:
    pass