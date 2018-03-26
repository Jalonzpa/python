#!/usr/bin/python
# run as python3
# make sure to download requests with 'pip3 install requests' before running the script!

import requests
dl = ""

print("What webpage do you want to download?\n\n1. Romeo and Juliet PDF\n2. HomeBot python script")
dl = int(input())    # sets the variable dl to an integer based on the user's input

if dl == 1:
    req = requests.get("https://automatetheboringstuff.com/files/rj.txt")    # var req is the value of the text of that page
    print("Ooh, good choice! Romeo and Juliet is waiting in this directory!")
    writeFile = open('RomeoAndJuliet.txt', 'wb') # opens the text file as write and binary
    for chunk in req.iter_content(100000):    # for every 100000 bytes of data
        writeFile.write(chunk)    # write the chunk of 100000 bytes to the file
elif dl == 2:
    req = requests.get("https://raw.githubusercontent.com/Jalonzpa/homebot_code/master/homebot.py")    # var req is the value of the text of that page
    print("The latest HomeBot python script is waiting in this directory.")
    writeFile = open('homebot.py', 'wb')    # opens the py file as write and binary
    for chunk in req.iter_content(100000):    # for every 100000 bytes
        writeFile.write(chunk)    # write that chunk to the file
