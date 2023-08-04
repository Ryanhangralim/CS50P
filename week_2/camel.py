camelCase = input("camelCase: ").strip(" ")
print("snake_case: ",end="")
for i in range(len(camelCase)):
    if camelCase[i].islower():
        print(camelCase[i],end="")
    else:
        print("_",camelCase[i].lower(), sep="",end="")