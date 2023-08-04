import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    result = ""
    if matches := re.search(
        r"^([1]?[0-9]):?([0-5][0-9])? (AM|PM) to ([1]?[0-9]):?([0-5][0-9])? (AM|PM)$",
        s
    ):
        group = matches.groups()
        if int(group[0]) > 12 or int(group[3]) > 12:
            raise ValueError
        new_from = new_format(group[0], group[1], group[2])
        new_until = new_format(group[3], group[4], group[5])
        return f"{new_from} to {new_until}"
    else:
        raise ValueError


def new_format(hour, minutes, am_pm):
    if am_pm == "AM":
        if int(hour) == 12:
            hour = "00"
        if minutes == None:
            return f"{int(hour):02d}:00"
        return f"{int(hour):02d}:{minutes}"
    if am_pm == "PM":
        if int(hour) >= 1 and int(hour) <= 11:
            hour = str(int(hour) + 12)
        if minutes == None:
            return f"{int(hour):02d}:00"
        return f"{int(hour):02d}:{minutes}"


if __name__ == "__main__":
    main()
