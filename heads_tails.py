import random 
options = ["head" , "tail"]
rounds = 5 
score = 0



while rounds > 0:
    coin_flipped = random.choice(options)
    users_guess = str(input("Take a guess (head) or (tail): ")).lower().strip()
    if users_guess == coin_flipped:
        print("you got it correct hurray ")
        score += 1       
    else:
        print(f"You got it wrong. The correct answer was {coin_flipped}.")
        
    rounds -= 1

print(f"Game over! Your final score is {score}.")
