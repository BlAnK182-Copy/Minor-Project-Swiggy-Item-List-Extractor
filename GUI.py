from tkinter import *
from extractor import Extractor
import consts as c
import pushToDB as ptd

class GUI:
    def __init__(self):

        self.window=Tk()

        self.greetingWidget=Label(self.window,text="Welcome to PESU Eateries!!")
        self.greetingWidget.pack()

        self.titleWidget=Label(self.window,text='Enter the name of the restaurant below.')
        self.titleWidget.pack()

        self.UrlEntryWidget=Entry(self.window,borderwidth='5')
        self.UrlEntryWidget.pack()
        
        self.restaurant_name=self.UrlEntryWidget.get()

        
        self.submitButton=Button(self.window,text="Submit",padx='50',fg='orange',bg='white',command=self.submitButtonClick)
        self.UrlEntryWidget.bind('<Return>',self.enterButton)
        self.submitButton.pack()

        self.window.mainloop()
            

    def submitButtonClick(self):
        # MyLabel2=Label(self.window,text="Here's the menu of "+self.UrlEntryWidget.get()+". Have a good meal!")
        # MyLabel2.pack()

        self.extractorObj = Extractor(
            restUrl = self.submission(),
            filename=c.FILENAME,
            maxLineLimit = c.MAX_LINE_LIMIT
        )
        self.sqlPushObject = ptd.Data_Operations()

        extractProcess = self.extractorObj.extract()

        if extractProcess == True:
            self.confirmationLabel=Label(self.window,text="Your response has been saved successfully.")
            self.sqlPushObject.createTable(c.FILENAME)
            self.sqlPushObject.add_items_to_table(c.FILENAME,c.FILENAME)
            self.tableConfirmationLabel = Label(self.window, text="Table created and appended into")
            self.tableConfirmationLabel.pack()

        else:
            self.confirmationLabel=Label(self.window,text="There was an error trying to access your url, please enter a valid url.")
        
        self.confirmationLabel.pack()

    def enterButton(self, event):
        self.submitButtonClick()
            
    def submission(self):
        return self.UrlEntryWidget.get()
