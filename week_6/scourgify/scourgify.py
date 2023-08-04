import sys
import csv
from tabulate import tabulate

if(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 3):
    sys.exit("Too many line arguments")

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

try:
    with open(sys.argv[2],"w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writeheader()
        for student in students:
            last_name, first_name = student["name"].split(",")
            writer.writerow({"first":first_name.strip(), "last":last_name.strip(), "house":student["house"]}) 
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[2]}")
