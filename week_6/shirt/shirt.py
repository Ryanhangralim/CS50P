import sys
import csv
from PIL import Image, ImageOps

if(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 3):
    sys.exit("Too many line arguments")

file_type = (".jpg",".jpeg","png")

if(not sys.argv[1].endswith(file_type)):
    sys.exit("Invalid Input")

input_name, input_type = sys.argv[1].split(".")
output_name, output_type = sys.argv[2].split(".")

if(not input_type == output_type):
    sys.exit("Input and output have different extensions")

menu = []
try:
    image_input = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    input_cropped = ImageOps.fit(image_input, shirt_size)
    input_cropped.paste(shirt, shirt)
    input_cropped.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not exist")
