state = "lagos"
button = str(input("do you want to start playing guessing game yes(Y)or no(N))")).lower()
while button == "y":
    print("what state was i born")
    guess = str(input("Type your guess here:")).lower()
    while guess != state:
         print("No, I was not born in ",guess,", try again ")
    else:
         print("Wow! That is a 1 out of 36 guess and you are right! I was born in ",guess, "!")
else:
    print("The Game has been shut Down")
    quit()
    