def main():
    output = value(input("Greeting: "))
    print(f"${output}")


def value(greeting):
    greeting = greeting.upper().strip(" ")
    if greeting[0] == "H":
        if greeting[0:5] == "HELLO":
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
