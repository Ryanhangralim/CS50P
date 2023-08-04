greeting = input("Greeting: ")

greeting = greeting.upper().strip(" ")
    
if(greeting[0]=='H'):
    if(greeting[0:5]=="HELLO"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")