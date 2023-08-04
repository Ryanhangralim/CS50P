import random

while True:
    try:
        level = int(input("Level: "))
        if (level >= 1) and (level <= 100):
            break
        continue
    except ValueError:
        continue

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        elif guess == answer:
            print("Just right!")
            break
    except ValueError:
        continue
