months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if('/' in date):
            date = date.split("/")
            if((int(date[0]))>12) or ((int(date[1]))>31):
                continue
            else:
                print(f"{int(date[2]):04}-{int(date[0]):02}-{int(date[1]):02}", end="")
                break
        else:
            date = date.split(" ")
            if date[0].title() not in months:
                continue
            if("," in date[1]):
                date[1] = date[1].replace(",","")
            else:
                continue
            if (int(date[1])>31):
                continue

            print(f"{int(date[2]):04}-{int(months.index(date[0].title())+1):02}-{int(date[1]):02}", end="")
            break
    except ValueError:
        continue
