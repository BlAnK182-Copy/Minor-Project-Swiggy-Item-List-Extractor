from tkinter import *
from tkinter import messagebox
from Assets.extractor import Extractor
import Assets.consts as c
import Assets.pushToDB as ptd
from Assets.Table_Generator import Table_Generator

class GUI:
    def __init__(self):

        self.window=Tk()

        self.windowHeight = c.WINDOW_HEIGHT
        self.windowWidth = c.WINDOW_WIDTH
        # self.window.resizable(width=TRUE, height=TRUE)
        self.window.geometry(f'{self.windowWidth}x{self.windowHeight}')
        # self.window.geometry("")
        # self.window.wm_attributes('-transparentcolor','black')

        #bgImage
        self.bgImage=PhotoImage(file=c.BG_IMAGE_PATH)
        self.bgImageLabel=Label(self.window,image=self.bgImage)
        self.bgImageLabel.grid(row=0,column=0, sticky="NSEW")

        #custom frame
        self.frame=Frame(self.window,height=f'{self.windowHeight * (1/2)}',width=f'{self.windowWidth * (1/2)}',bg='orange')
        self.frame.grid(row=0,column=0, padx=(self.windowWidth * (1/4)), pady=(self.windowHeight * (1/4)))

        #greeting 
        self.greetingWidget=Label(self.frame,text="Welcome to PESU Eateries!!",font="Consolas 24 bold italic", bg = None)
        self.greetingWidget.grid(row = 0, column = 0, padx = c.X_PADDING, pady = c.Y_PADDING)

        #title
        self.titleWidget=Label(self.frame,text='Enter the Swiggy-URL of the restaurant:',font='Courier 8')
        self.titleWidget.grid(row = 1, column = 0, padx = c.X_PADDING)
        
        #url entry
        self.UrlEntryWidget=Entry(self.frame,borderwidth='0')
        self.UrlEntryWidget.grid(row = 2, column= 0, padx = c.X_PADDING)
        
        self.restaurant_name=self.UrlEntryWidget.get()

        self.submitButtonImage=PhotoImage(file=c.BUTTON_IMAGE_PATH)
        self.submitButton=Button(self.frame,image=self.submitButtonImage,command=self.submitButtonClick,border=0)
        self.UrlEntryWidget.bind('<Return>',self.enterButton)
        self.submitButton.grid(row = 3, column=0, padx=c.X_PADDING, pady=c.Y_PADDING)

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
            tableCreated = self.sqlPushObject.createTable(c.FILENAME)
            if tableCreated:
                self.sqlPushObject.add_items_to_table(c.FILENAME,c.FILE_STORAGE + c.FILENAME)
            messagebox.showinfo("Notification!",f"Your response has been saved succesfully into {c.FILENAME}.txt. Table created and appended into.")

            #temporaily calling a tksheet
            self.table = Table_Generator()
            root = Tk()
            table1= self.table.get_all_contents(root,c.FILENAME, display_category=True)
            table1.pack()


        else:
            messagebox.showinfo("ERROR!!","There was an error trying to access your url, please enter a valid url.")

    def enterButton(self, event):
        self.submitButtonClick()
            
    def submission(self):
        return self.UrlEntryWidget.get()
