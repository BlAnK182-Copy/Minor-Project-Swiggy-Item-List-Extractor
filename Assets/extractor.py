#Minor Project - Swiggy Item List and Prices extractor.

import urllib.request
import os
import Assets.consts as c

class Extractor:

    def __init__(self, restUrl, filename, maxLineLimit):
        #installing bs4 if not present
        try:
            from bs4 import BeautifulSoup

        except ModuleNotFoundError:
            os.system("pip install bs4")
            from bs4 import BeautifulSoup

        if c.FILE_DIR_NAME.lower() not in [i.lower() for i in os.listdir(c.OUTER_FOLDER)]:
            os.mkdir(c.FILE_STORAGE)

        self.dirPath = c.FILE_STORAGE
        print(self.dirPath)
        self.filename = filename + ".html"
        self.filePath = self.dirPath+self.filename
        self.urlToRetrieve = restUrl
        self.maxLimitOfLine = maxLineLimit

    def extract(self):

        try:

            urllib.request.urlretrieve(self.urlToRetrieve,self.filePath) #retrieving html file

            self.txtFile = open(self.filePath.rstrip(".html")+".txt", 'w')

            self.totalNumOfItems = 0

            #retrieving prices and items
            with open(self.filePath) as fileParser:
                self.soup = BeautifulSoup(fileParser, "html.parser")
        
        
                for h2 in self.soup.findAll("h2", {"class":"M_o7R"}):

                    self.itemNames = []
                    self.itemPrices = []

                    self.txtFile.write(h2.string + "\n")
                    self.txtFile.write("\n")

                    for h3 in h2.parent.findAll("h3", {"class":"styles_itemNameText__3ZmZZ"}):
                        self.itemNames.append(h3.string)
                    
                    for span in h2.parent.findAll("span", {"class":"rupee"}):
                        self.itemPrices.append(span.string)
                    
                    self.numCatItems = len(self.itemNames)

                    for i in range(0, self.numCatItems):
                        self.numSpaces = self.maxLimitOfLine - (len(self.itemNames[i]) + len(self.itemPrices[i]))
                        self.toWrite =  self.itemNames[i] + chr(32) * self.numSpaces + self.itemPrices[i] + "\n"
                        self.txtFile.write(self.toWrite)
                        self.totalNumOfItems+=1

                    self.txtFile.write("\n")

            self.txtFile.write(f"Total Number of Items: {self.totalNumOfItems}")
            self.txtFile.close()

            print(f"Made {self.filename.rstrip('.html')+'.txt'} and appended items into it.")
            os.remove(self.filePath)
            return True
        
        except:
            print(f"Error finding URL: {self.urlToRetrieve}, check if it is valid.")
            return False