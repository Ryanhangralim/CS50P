def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    decimal = 0
    char = 0
            
    for i in range(len(s)):
        if(s[i].isdecimal()):
            decimal += 1
        else:
            char += 1
            
    if(len(s)>=2 and len(s)<=6):
        if(char==len(s)):
            return True
        if(not s[0:char].isdecimal()):
            if(s[char:len(s)].isdecimal()):
                if(s[char]!="0"):
                    return True
    return False

main()