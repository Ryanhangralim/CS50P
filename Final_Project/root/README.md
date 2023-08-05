# **YouTube to MP3 Downloader**
### **Video Demo:** https://drive.google.com/file/d/1O-iY1mD_zjnjBhR4RwIWuRucMb1X5W6x/view?usp=sharing
### **Description :** 
- **About This Project**

    The idea of this project came from the problem I face in my daily life. So, a little background story, I have an MP3 Player filled with songs and podcasts so I can listen to it while driving to college or doing other work without having to have my phone around me all the time

    The problem emerged when I want to fill the MP3 player with new songs or podcasts. I would have to go to YouTube, pick the song/podcast, copy the link and use a third-party website to download it as an MP3 file.

    After completing the CS50P course, I learned that I could make a program to help with this problem. I searched for a library to download files from YouTube and encountered the `pytube` library.

    With the help of `pytube`, I created a project to help me with this problem. This program helps user to easily download YouTube videos from video URL to an MP3 file which could be used for various purposes, in my case for an MP3 Player.

    The 2 main features in this project is "Single Link" and "Multiple Links". "Single link" allows user to input YouTube video link and a custom output file name if the user wants to. Then it will download the video as an MP3 file while "Multiple Links" allows user to input a text file(.txt) which is filled with links of  YouTube videos. The program will then download all the video in the file as an MP3 file.

    The program is also constructed with user input validation (links and file output name) and exception handling so that user doesn't get confused with cryptic messages.
- File In Project

    This project consists of 2 files:
    1. project.py

        This file is the main file where all the functions are stored. All you need to do to use the program is to run this file with "python project.py"
    2. test_project.py
        This file's purpose is to test the input validation functions in "project.py"

