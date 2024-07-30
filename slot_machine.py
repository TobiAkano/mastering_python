#Main things we need to do in this project 
#1 collect users deposit
#allow user to bet on the on the first or second or third 
# multiply bet by the value of the line add to their balance 
# 
import random
spin = False
slot_fruits = ["single_bar", "double_bar", "triple_bar", "cherry", "seven"]



def transactions():
    global cash_deposit
    cash_deposit = int(input("How much would you like to insert: "))
    
def status_program():
    global bet
    bet = int(input(f"How much from your deposite of ${cash_deposit} would you like to use to bet: "))
    print(f"""

⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⢸⣿⣿⠛⠻⣿⣿
⣿⣿⣿⣿⣿⣿⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣤⣿⣿
⣿⣿⣿⣿⣿⣿⡇⣿⡇⠀⠀⠘⠋⠀⠙⠋⠀⠘⠋⠀⠘⠋⠀⢸⣿⣿⠈⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⣿⡇⢀⡀⢠⡀⢀⡀⢠⡀⢀⡀⢠⡀⢀⡀⢸⣿⠁⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢸⣿⠀⢀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿
""")
    
    while True:
        spin_status = str(input("Do you want to spin the Reel (YES) or (NO)")).lower().strip()
        if spin_status == "yes":
            spin == True
            break
        elif spin_status == "no":
            spin_status == False
            quit()
        else:
            print("Enter a valid Input")
def reel_generator():
    global reel
    global column1 
    global column2
    global column3
    column1 = random.choice(slot_fruits)
    column2 = random.choice(slot_fruits)
    column3 = random.choice(slot_fruits)
    print(f"Reels: {column1} | {column2} | {column3}")


def payout_system():
    payouts = {
        "single_bar": 2,
        "double_bar": 5,
        "triple_bar": 10,
        "cherry": 15,
        "seven": 50
    }        

    payout = 0
    if column1 == column2 == column3:
        payout = bet * payouts[column1]
    elif column1 == "single_bar" or column2 == "single_bar" or column3 == "single_bar":
        payout = bet * payouts["single_bar"]
    elif column1 == "double_bar" or column2 == "double_bar" or column3 == "double_bar":
        payout = bet * payouts["double_bar"]
    elif column1 == "triple_bar" or column2 == "triple_bar" or column3 == "triple_bar":
        payout = bet * payouts["triple_bar"]
    elif column1 == "cherry" or column2 == "cherry" or column3 == "cherry":
        payout = bet * payouts["cherry"]
    elif column1 == "seven" or column2 == "seven" or column3 == "seven":
        payout = bet * payouts["seven"]

    # payout
    if payout > 0:
        print(f"You won {payout} credits!")
    else:
        print("You didn't win this time. Try again!")
    

def main():
    status_program()
   
    while True:
        transactions()
        reel_generator()
        payout_system()

main()


