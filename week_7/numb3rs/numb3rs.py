import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if (
            is_valid(int(matches.group(1)))
            and is_valid(int(matches.group(2)))
            and is_valid(int(matches.group(3)))
            and is_valid(int(matches.group(4)))
        ):
            return True
    return False


def is_valid(num):
    if num >= 0 and num <= 255:
        return True
    return False


if __name__ == "__main__":
    main()
