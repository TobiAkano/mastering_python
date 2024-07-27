import random
lives = 10 
print("welcome to guessing game")
print("type two values you want the number to be between")

first_value = int(input("type the first number here >: "))
second_value = int(input("type the second number here >: "))

random_number = random.randint(first_value , second_value)

print(f"guess a number between {first_value} and {second_value }")

while lives > 0:
    user_guess = int(input("write your guess here: "))
    if user_guess == random_number:
        print("you guess it correctly, hurrayy!!! ")
        print(f"you guessed it with only {10-lives} tries ")
    else:
        print("you guesss it wrongly")
        lives -= 1
        if lives == 0:
            quit()
    