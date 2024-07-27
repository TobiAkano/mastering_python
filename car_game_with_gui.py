data = 1
started = False
while data == 1:
    action = str(input("Type your action here:")).lower()
    if action == "start":
        if started:
            print("your car has already started ")
        else:
            started = True
            print("your car started")
    if action == "stop":
        # if not started
        print("your car stoped")
        
    if action == "help":
        print("""
        start- to move the car 
        stop - to stop the car
        exit - to get out from the car
        """)
    else:
        print("I dont understand That")
    

