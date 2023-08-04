answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

if answer.strip(" ") == "42":
    print("Yes")
elif (answer.upper() == "FORTY TWO") or (answer.upper() == "FORTY-TWO"):
    print("Yes")
else:
    print("No")