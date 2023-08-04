import re

def main():
    link = "https://www.youtube.com/watch?v=fJ9rUzIMcZQ&pp=ygUFcXVlZW4%3D"
    link = link.strip()
    if(is_ValidLink(123)):
        print("Valid")
    else:
        print("Invalid")


def is_ValidLink(link):
    try:
        if re.search(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$", link):
            return True
        else:
            return False
    except BaseException:
        return False



def is_ValidOutputName(output):
    pass


def download_Audio(link):
    pass


def single_File():
    pass


def multi_File():
    pass


if __name__ == "__main__":
    main()