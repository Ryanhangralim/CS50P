while True:
    try:
        fraction = input("Fraction: ").strip(" ")
        fraction = fraction.split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        fraction = x/y
        if(x>y):
            continue
        break
    except (ValueError, ZeroDivisionError):
        pass 
            
percentage = round((100/y)*x)
if(percentage <= 1):
    print("E")
elif(percentage > 1 and percentage < 99):
    print(f"{percentage}%")
elif(percentage >= 99):
    print("F")
            
