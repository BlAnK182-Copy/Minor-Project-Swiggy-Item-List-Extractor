#Minor Project - Swiggy Item List and Prices extractor.

#modules
import urllib.request
import os 
import json

#installing bs4 if not present
os.system("pip install bs4")
from bs4 import BeautifulSoup

#consts
DIR_PATH = __file__.rstrip(os.path.basename(__file__))
FILENAME = "index.html"
FILE_PATH = DIR_PATH+FILENAME
URL_TO_RETRIEVE = "https://www.swiggy.com/restaurants/kitchen-6-1st-main-4th-phase-yelahanka-new-town-bangalore-31219"
MAX_LIMIT_OF_LINE = 75


#retrieving html file
urllib.request.urlretrieve(URL_TO_RETRIEVE,FILE_PATH)

#text file to append into
txtFile = open(FILE_PATH.rstrip(".html")+".txt", 'w')

#retrieving prices and items
totalNumOfItems = 0

with open(FILE_PATH) as fileParser:
    soup = BeautifulSoup(fileParser, "html.parser")


    for h2 in soup.findAll("h2", {"class":"M_o7R"}):

        itemNames = []
        itemPrices = []

        txtFile.write(h2.string + "\n")
        txtFile.write("\n")

        for h3 in h2.parent.findAll("h3", {"class":"styles_itemNameText__3bcKX"}):
            itemNames.append(h3.string)
        
        for span in h2.parent.findAll("span", {"class":"rupee"}):
            itemPrices.append(span.string)
        
        numCatItems = len(itemNames)

        for i in range(0, numCatItems):
            numSpaces = MAX_LIMIT_OF_LINE - (len(itemNames[i]) + len(itemPrices[i]))
            toWrite =  itemNames[i] + chr(32) * numSpaces + itemPrices[i] + "\n"
            txtFile.write(toWrite)
            totalNumOfItems+=1

        txtFile.write("\n")

txtFile.write(f"Total Number of Items: {totalNumOfItems}")
txtFile.close()

print(f"Made {FILENAME.rstrip('.html')+'.txt'} and appended items into it.")