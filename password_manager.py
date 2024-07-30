from test6 import user_greeting
name = str(input("what is your name"))
user_greeting(name)
master_password = input("Type the password here: ")
def add():
    username = (input("Type your username of the account here: "))
    pwd = (input("Type your password here: "))
    with open("password.txt" , "a") as f:
        f.write(name + "|" + pwd)

def veiw():
    pass

while True:
    option = str(input("Would you like to add and account or veiw and account: "))
    if option == "add":
        continue
    if option == "veiw":
        continue
