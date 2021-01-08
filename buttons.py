from tkinter import *

class ButtonCustomize(Button):
    def __init__(self,root,text,row,col):
        super().__init__(root,text=text)
        self.grid(row=row,column=col,padx=10,pady=10)
    def add_function(self,func,id,movie,year,director,password,comment):
        self.config(command=lambda:func(id,movie,year,director,password,comment))


class InputCustomize(Entry):
    def __init__(self,root,row,col):
        super().__init__(root)
        self.grid(row=row,column=col,padx=10,pady=10)
        self.config(justify=CENTER)


