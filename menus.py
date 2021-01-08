from tkinter import *

class Barmenu(Menu):
    def __init__(self,root):
        super().__init__(root)
        root.config(menu=self,width=300,height=400)
    def add_menu(self,nameMenu,menu):
        self.add_cascade(label=nameMenu, menu=menu)

class Menudb(Menu):
    def __init__(self,bar,root,*args):
        super().__init__(bar, tearoff=0)
        self.add_command(label="Connect",command=args[0])
        self.add_command(label="Exit",command=lambda:args[1](root))

class Menudelete(Menu):
    def __init__(self,bar):
        super().__init__(bar, tearoff=0)
    def add_function_clear(self,func,textBox,*args):
        self.add_command(label="Clear",command=lambda:func(textBox,*args))

class Menucrud(Menu):
    def __init__(self,bar,*args):
        super().__init__(bar, tearoff=0)
    def add_function_create(self,func,id,movie,year,director,password,comment):
        self.add_command(label="Create",command=lambda:func(id,movie,year,director,password,comment))
    def add_function_read(self,func,id,movie,year,director,password,comment):
        self.add_command(label="Read",command=lambda:func(id,movie,year,director,password,comment)) 
    def add_function_update(self,func,id,movie,year,director,password,comment):
        self.add_command(label="Update",command=lambda:func(id,movie,year,director,password,comment))    
    def add_function_delete(self,func,id,movie,year,director,password,comment):
        self.add_command(label="Delete",command=lambda:func(id,movie,year,director,password,comment))    

class Menuabout(Menu):
    def __init__(self,bar,*args):
        super().__init__(bar, tearoff=0)
        self.add_command(label="About",command=args[0])
        self.add_command(label="License",command=args[1])