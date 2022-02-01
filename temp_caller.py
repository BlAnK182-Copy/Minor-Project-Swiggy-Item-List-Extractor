from Table_Generator import Table_Generator 

from tkinter import *

table= Table_Generator()

#This is a temporary main to call and test the functions in Table_Generator

root = Tk()

table1= table.get_contents_with_keyword(root,"menu1","chicken", display_category=TRUE)
table1.pack()


root.mainloop()