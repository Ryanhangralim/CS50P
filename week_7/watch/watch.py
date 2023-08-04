import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'src="([a-z0-9:/\.]*)"', s, re.IGNORECASE):
        if url := re.search(r"^(?:https?)://(?:www\.)?youtube\.com/embed/([a-z0-9]+)$",matches.group(1),re.IGNORECASE): 
            return f"https://youtu.be/{url.group(1)}"
        else:
            return None

if __name__ == "__main__":
    main()