import sys
import csv
from tabulate import tabulate

if(len(sys.argv) == 1):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 2):
    sys.exit("Too many line arguments")

if(not sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")
menu = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for pizza, small, big in reader:
            menu.append({"pizza": pizza, "small": small, "big":big})
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers="firstrow", tablefmt="grid"))