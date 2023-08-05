"""
Project Title : YouTube to MP3 Downloader
Name : Ryan Hangralim
City : Denpasar, Bali
Country : Indonesia
"""

import re
from pyfiglet import Figlet
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

figlet = Figlet()


def main():
    while True:
        print("YouTube to MP3 Downloader Menu")
        print("Link Input:")
        print("[1] Single Link")
        print("[2] Multiple Links")
        print("[3] Exit")
        choice = input("Choice: ")

        match choice:
            case "1":
                single_File()
            case "2":
                multi_File()
            case "3":
                break
            case _:
                print("Invalid Choice")
    figlet.setFont(font="big")
    print(figlet.renderText("This Was CS50"))


def is_ValidLink(link):
    try:
        if re.search(
            r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$",
            link,
        ):
            return True
        else:
            return False
    except BaseException:
        return False


def is_ValidOutputName(output):
    try:
        if re.search(r"^[a-z0-9\-_ ]+$", output, re.IGNORECASE):
            return True
        else:
            return False
    except BaseException:
        return False


def download_Audio(link, output_name=None):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_by_itag(251)
        if not output_name == None:
            stream.download(filename=f"{output_name}.mp3")
            print("Audio Downloaded")
        else:
            stream.download(filename=f"{yt.title}.mp3")
            print("Audio Downloaded")
    except VideoUnavailable:
        print(f"Video {link} is unavailable")


def is_ValidFile(file):
    try:
        if re.search(r"([a-z0-9_\- ])+\.txt", file, re.IGNORECASE):
            return True
        else:
            return False
    except BaseException:
        return False


def single_File():
    try:
        #getting video link from user input
        while True:
            link = input("Video Link: ")
            if is_ValidLink(link):
                break
            else:
                print("Invalid Link")

        #getting output name from user input
        while True:
            output = input("Output name (0 for default): ")
            if output == "0":
                break
            elif is_ValidOutputName(output):
                break
            else:
                print("Invalid Output")

        if output == "0":
            output = None

        download_Audio(link, output)

    except BaseException:
        print("Invalid")
        pass


def multi_File():
    while True:
        try:
            file_input = input("Text file(.txt) with youtube links: ").strip()
            if file_input == "0":
                break

            # validate user input
            if is_ValidFile(file_input):
                with open(file_input, "r") as file:
                    links = file.readlines()

            # iterating through file and downloading audio files
            for i in range(len(links)):
                link = links[i].strip()
                if is_ValidLink(link):
                    download_Audio(link)
                else:
                    print("Invalid Link, Skipping to Next Link")
                    continue
            break
        except FileNotFoundError:
            print("File Not Found, Try Again! (0 to return)")


if __name__ == "__main__":
    main()
