def main():
    time = input("What time is it? ")
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

if __name__ == "__main__":
    main()