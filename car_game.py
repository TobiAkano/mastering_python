print("welocome to Car Racing Simulator ")
car = input("What car would you like to drive ?").upper()
print(f"a {car} just spawned in your garage ")
started = False
parked = False
while True:
    action = input(" what would you like to do with the car ")
    if action == "start":
        print(f"your {car} engine has started  ")
        while action == "start":
            if action =="location":
                location = input("where would you want to go")
                print (f"your {car}has arrived at {location}")
            elif started:
                print ("your car has already started")
                ...
            
    elif action == "park":
        print("your {car} has been parked")
        parked = True
    elif action == "stop" :
        print(f" your {car} engine was switched off")
    elif action == "help" :
        print(""" start - to start the car engine
            
            """)
    elif action == "quit":
        ...

    else:
        print ("your car doesnt have that feature")

