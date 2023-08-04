input_string = input("Input: ")
print("Output: ",end="")
for i in range(len(input_string)):
    char = input_string[i].lower()
    if(char == "a" or char =="i" or char == "u" or char == "e" or char == "o"):
        continue
    else:
        print(input_string[i], end="")
