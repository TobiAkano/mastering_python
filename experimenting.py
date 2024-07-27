password = "cool"
guess = input("Enter password here:")
chances = 4
while guess != password:
    print("incorect password, try again")
    guess = str(input("Enter password here:"))
    chances = chances - 1 
    print("you have ", chances, "more chances")
    if chances == 0:
        print("you ran out of tries")
        exit()

    
else:
    print("you got it , hurrays")