import inflect
import sys
from datetime import timedelta, date, datetime

p = inflect.engine()


def main():
    date_of_birth = input("Date of birth: ")
    year, month, day = check_date(date_of_birth)
    date_of_birth = date(int(year), int(month), int(day))
    present_date = date.today()
    diff = present_date - date_of_birth
    total_minutes = diff.days * 24 * 60
    result = p.number_to_words(total_minutes, andword="")
    print(f"{result.capitalize()} minutes")


def check_date(s):
    try:
        if datetime.strptime(s, "%Y-%m-%d"):
            return s.split("-")
    except BaseException:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
