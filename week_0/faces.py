def convert (string):
    string = string.replace(":)", "🙂").replace(":(","🙁")
    return string

def main():
    message = convert(input(""))
    print(message)

main()