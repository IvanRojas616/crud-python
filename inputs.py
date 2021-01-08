from tkinter import *

class LabelCustomize(Label):
    def __init__(self,root,text,row,col):
        super().__init__(root,text=text,padx=10,pady=10)
        self.grid(row=row,column=col)

class InputCustomize(Entry):
    def __init__(self,root,row,col):
        super().__init__(root)
        self.grid(row=row,column=col,padx=10,pady=10)
        self.config(justify=CENTER)


