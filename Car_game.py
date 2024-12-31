commnd = ""
start_paramter = True
stop_parameter = False
start = False
while True:
    commnd = input(">").lower()
    if commnd == "start":
        if start:
            print("car is already started!")
        else:
            start = True
            print("Car Started ...")
    elif commnd == "stop":
        if not start:
            print("the is already stopped!")
        else:
            start = False
            print( "Car Stopped ..." )
    elif commnd == "help" :
        print('''
start - start the car
stop - stop the car
quit - quit the program        
        ''')
    elif commnd == "quit" :
        break
    else:
        print( "I Don't understand " )