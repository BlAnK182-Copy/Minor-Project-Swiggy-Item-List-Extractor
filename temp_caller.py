from Assets.Table_Generator import Table_Generator 

from tkinter import *
import Assets.consts as c

table= Table_Generator()

#This is a temporary main to call and test the functions in Table_Generator

root = Tk()

table1= table.get_all_contents(root,c.FILENAME, display_category=True)
table1.pack()

root.mainloop()