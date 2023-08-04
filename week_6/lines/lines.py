import sys

if(len(sys.argv) == 1):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 2):
    sys.exit("Too many line arguments")

if(not sys.argv[1].endswith(".py")):
    sys.exit("Not a Python file")
line_count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if(line.strip().startswith("#") or line.isspace()):
                continue
            else:
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)