from tkinter import *

root=Tk()

MyLabel=Label(root,text="Welcome to PESU Eateries!!")
MyLabel.pack()

MyLabel1=Label(root,text='Enter the name of the restaurant below.')
MyLabel1.pack()

E=Entry(root,borderwidth='5')
E.pack()
restaurant_name=E.get()

def myClick():
    MyLabel2=Label(root,text="Here's the menu of "+E.get()+". Have a good meal!")
    MyLabel2.pack()

def clicker(event):
    myClick()
    MyLabel3=Label(root,text="Your response has been saved successfully.")
    MyLabel3.pack()


Button1=Button(root,text="Submit",padx='50',fg='orange',bg='white',command=myClick)
E.bind('<Return>',clicker)
Button1.pack()

root.mainloop()
