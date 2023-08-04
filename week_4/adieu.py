import inflect

p = inflect.engine()

list = []

while True:
    try:
        word = input("Name: ")
        list.append(word)
    except(KeyboardInterrupt,EOFError):
        print()
        break

print(f"Adieu, adieu, to {p.join(list)}")