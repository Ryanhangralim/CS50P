def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    fraction.strip(" ")
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percentage = round((100/y)*x)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else: 
        return f"{percentage}%"

if __name__ == "__main__":
    main()