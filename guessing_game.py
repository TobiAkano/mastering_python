import random as rand

def welcome(name):
    name = str(input("what is your name: ")).upper
    print(f"{name} welcome to Maxion Guessing game")

def scoring_system(user_guess):

    rand_numb = rand.randint(1,10)

    user_guess =(int(input("Guess the number")))
    if user_guess !=  rand_numb:
        print("try again that wrong")
    else:
        print("hurrayyyyyy !!!! you got it")
        
    return user_guess
    
    









