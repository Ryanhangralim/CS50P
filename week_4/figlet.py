from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(f"Output: {figlet.renderText(user_input)}")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(f"Output: {figlet.renderText(user_input)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")