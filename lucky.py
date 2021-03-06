#!/usr/bin/python
# run as python3
# THIS IS NOT MY ORIGINAL CODE: most of it was taken from https://automatetheboringstuff.com/chapter11/. I am only using it to educate myself.
# make sure to download the requests and bs4 modules before running this script with 'pip3 install requests' and 'pip3 install bs4'

import requests, sys, webbrowser, bs4

print("Googling...")    # display text while downloading the Google page
req = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

results = bs4.BeautifulSoup(req.text)    #retrieve top search results and store them in results variable
linkElems = results.select('.r a')

numOpen = min(5, len(linkElems))    # find number of links
for i in range(numOpen):    # on each iteration the program opens a new tab from the linkElems variable
    webbrowser.open('http://google.com' + linkElems[i].get('href'))    # opens browser tab for each result

print("Done.")
