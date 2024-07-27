secret_number = 9
number_of_guesses = 0
guess_limit = 3
while number_of_guesses < guess_limit:
    guess = int(input("Guess :"))
    number_of_guesses += 1
    if guess == secret_number:
        print("You Got the number Hurray !!!!!")
        break
else:
    ...