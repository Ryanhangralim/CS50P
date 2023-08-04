grocery_list = {}

while True: 
    try:
        item = input().strip().upper()
        if not item in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
    except (EOFError, KeyboardInterrupt):
        print()
        break

for item in sorted(grocery_list):
    print(grocery_list[item],item)
    