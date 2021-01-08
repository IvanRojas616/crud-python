from tkinter import *
from tkinter import messagebox
from menus import *
from inputs import *
from buttons import *
from logic import *

root = Tk()
root.title("Movies CRUD")
img = PhotoImage(file='C:/Users/Ivan rojas/Documents/Python/crud-practice/icon.png')
root.iconphoto(False,img)
frameInputs = Frame(root)
frameInputs.pack()
frameButtons = Frame(root)
frameButtons.pack()

#Bar
barmenu = Barmenu(root)
#Menus
dbMenu = Menudb(barmenu,root,connectDB,exitApp)
deleteMenu = Menudelete(barmenu)
crudMenu = Menucrud(barmenu)
aboutMenu = Menuabout(barmenu,about,showLicense)
#Add menus to menubar
barmenu.add_menu("DB",dbMenu)
barmenu.add_menu("Clear",deleteMenu)
barmenu.add_menu("CRUD",crudMenu)
barmenu.add_menu("Help",aboutMenu)

#Labels
lblid = LabelCustomize(frameInputs,"Id",0,0)
lblmovie = LabelCustomize(frameInputs,"Movie Name",1,0)
lblyear = LabelCustomize(frameInputs,"Year",2,0)
lbldirector = LabelCustomize(frameInputs,"Director",3,0)
lblpass = LabelCustomize(frameInputs,"Access Passsword",4,0)
lblcomment = LabelCustomize(frameInputs,"Comment",5,0)

#Inputs
id = InputCustomize(frameInputs,0,1)
movie = InputCustomize(frameInputs,1,1)
year = InputCustomize(frameInputs,2,1)
director = InputCustomize(frameInputs,3,1)
password = InputCustomize(frameInputs,4,1)
password.config(show="*")
comment = Text(frameInputs,width=20,height=10,wrap=WORD)
comment.grid(row=5,column=1,padx=10,pady=10)
scroll = Scrollbar(frameInputs,command=comment.yview)
scroll.grid(row=5,column=2,sticky="nsew")
comment.config(yscrollcommand=scroll.set)

#Add function clear
deleteMenu.add_function_clear(clear,comment,id,movie,year,director,password)

#Add function create
crudMenu.add_function_create(insert,id,movie,year,director,password,comment)
#Add function read
crudMenu.add_function_read(read,id,movie,year,director,password,comment)
#Add function update
crudMenu.add_function_update(update,id,movie,year,director,password,comment)
#Add function delete
crudMenu.add_function_delete(delete,id,movie,year,director,password,comment)
#Buttons
createB = ButtonCustomize(frameButtons,"Create",0,0)
createB.add_function(insert,id,movie,year,director,password,comment)
readB = ButtonCustomize(frameButtons,"Read",0,1)
readB.add_function(read,id,movie,year,director,password,comment)
updateB = ButtonCustomize(frameButtons,"Update",0,2)
updateB.add_function(update,id,movie,year,director,password,comment)
deleteB = ButtonCustomize(frameButtons,"Delete",0,3)
deleteB.add_function(delete,id,movie,year,director,password,comment)

root.mainloop()