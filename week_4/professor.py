import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        tries = 0
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
                continue
        if tries == 3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
            continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, int(str(9) * level))
    elif level == 2:
        return random.randint(10, int(str(9) * level))
    elif level == 3:
        return random.randint(100, int(str(9) * level))


if __name__ == "__main__":
    main()
