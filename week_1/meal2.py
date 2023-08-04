def main():
    time = input("What time is it? ")
    if(time.endswith("a.m.")):
        time_float = convert2(time)
    elif(time.endswith("p.m.")):
        time_float = convert2(time)
    else:
        time_float = convert(time)
        
    if(time_float>=7.0 and time_float<= 8.0):
        print("breakfast time")
    elif(time_float>=12.0 and time_float<= 13.0):
        print("lunch time")
    elif(time_float>=18.0 and time_float<= 19.0):
        print("dinner time")
    

def convert(time):
    time = time.strip(" ")
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours+minutes

def convert2(time2):
    time = time2.removesuffix('a.m.').removesuffix('p.m.')
    time = time.strip(" ")
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    if(time2.endswith("p.m.")):
        hours += 12
    return hours+minutes
    
if __name__ == "__main__":
    main()