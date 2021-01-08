from sqlite3 import *
from tkinter import messagebox
from tkinter import *
"""
DB Menu
"""
#Database connection
def connectDB():
    conn = None
    cursor = None
    try:
        conn = connect("movies")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE movies 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            moviename VARCHAR(30),
            year INT(4),
            director VARCHAR(20),
            password VARCHAR(20),
            comment VARCHAR(200))
            """)

        messagebox.showinfo("Database Connection","Database created")
    except Exception as e:
        messagebox.showwarning("Attention","Datbase exists already!!!")
    finally:
        cursor.close()
        conn.close()
#Exit app
def exitApp(root):
    salir = messagebox.askyesno("Exit","Are you sure ?")
    if salir:
        root.destroy()

"""
Clear Menu
"""
def clear(textBox,*args):
    textBox.delete("1.0",END)
    for i in args:
        i.delete("0",END) 

"""
CRUD Menu
"""
def insert(idEntry,movieEntry,yearEntry,directorEntry,passEntry,comment):
    conn = None
    cursor = None
    try:
        isNumber = yearEntry.get().isdigit() and len(yearEntry.get()) == 4  
        if movieEntry.get() and isNumber and directorEntry.get() and passEntry.get():
            conn = connect("movies")
            cursor = conn.cursor()
            #This is recomended, for avoid SQL Injection
            cursor.execute("INSERT INTO movies VALUES(NULL,?,?,?,?,?)",
            ((movieEntry.get(),yearEntry.get(),directorEntry.get()
            ,passEntry.get(),comment.get("1.0",END))))
            conn.commit()
            idEntry.delete("0",END)
            movieEntry.delete("0",END)
            yearEntry.delete("0",END)
            directorEntry.delete("0",END)
            passEntry.delete("0",END)
            comment.delete("1.0",END)
            messagebox.showinfo("Create","Created Successfully")
        else:
            raise ValueError()
    except Error as e:
        messagebox.showerror("Err","Database Create Error!!!")
    except ValueError as e:
        messagebox.showerror("Error","Create Error, verify fields's content !!!")
    else:
        cursor.close()
        conn.close()
def read(idEntry,movieEntry,yearEntry,directorEntry,passEntry,comment):
    conn = None
    cursor = None
    try:
        if idEntry.get():
            conn = connect("movies")
            cursor = conn.cursor()
            #This is recomended, for avoid SQL Injection
            cursor.execute("SELECT * FROM movies WHERE id=?",
            ((idEntry.get())))
            result = cursor.fetchall()
            #result is a multidimensional list
            if result:
                idEntry.delete("0",END)
                idEntry.insert("0",str(result[0][0]))
                movieEntry.delete("0",END)
                movieEntry.insert("0",str(result[0][1]))
                yearEntry.delete("0",END)
                yearEntry.insert("0",str(result[0][2]))
                directorEntry.delete("0",END)
                directorEntry.insert("0",str(result[0][3]))
                passEntry.delete("0",END)
                passEntry.insert("0",str(result[0][4]))
                comment.delete("1.0",END)
                comment.insert("1.0",str(result[0][5]))
            else:
                raise Exception()
    except Exception as e:
        messagebox.showerror("Err","Database Read Error!!!")
    else:
        cursor.close()
        conn.close()
def update(idEntry,movieEntry,yearEntry,directorEntry,passEntry,comment):
    conn = None
    cursor = None
    try:
        if idEntry.get():
            conn = connect("movies")
            cursor = conn.cursor()
            #This is recomended, for avoid SQL Injection
            cursor.execute("UPDATE movies SET moviename=?,year=?,director=?,password=?,comment=? WHERE id=?",
            ((movieEntry.get(),yearEntry.get(),directorEntry.get(),passEntry.get(),comment.get("1.0",END),idEntry.get())))
            conn.commit()
            idEntry.delete("0",END)
            movieEntry.delete("0",END)
            yearEntry.delete("0",END)
            directorEntry.delete("0",END)
            passEntry.delete("0",END)
            comment.delete("1.0",END)
            print(cursor.rowcount)
            if cursor.rowcount:
                messagebox.showinfo("Create","Updated Successfully")
            else:
                raise Exception()
    except Exception as e:
        messagebox.showerror("Err","Database Updated Error!!!")
        print(e.args)
    else:
        cursor.close()
        conn.close()
def delete(idEntry,movieEntry,yearEntry,directorEntry,passEntry,comment):
    conn = None
    cursor = None
    try:
        if idEntry.get():
            conn = connect("movies")
            cursor = conn.cursor()
            #This is recomended, for avoid SQL Injection
            cursor.execute("DELETE FROM movies WHERE id=?",
            ((idEntry.get())))
            conn.commit()
            idEntry.delete("0",END)
            movieEntry.delete("0",END)
            yearEntry.delete("0",END)
            directorEntry.delete("0",END)
            passEntry.delete("0",END)
            comment.delete("1.0",END)
            if cursor.rowcount:
                messagebox.showinfo("Create","Deleted Successfully")
            else:
                raise Exception()
    except Exception as e:
        messagebox.showerror("Err","Database Deleted Error!!!")
        print(e.args)
    else:
        cursor.close()
        conn.close()
"""
Help Menu
"""
def showLicense():
    messagebox.showinfo("License","Sofware distributed under MIT LICENSE.\n You can modify the code like you want.")
def about():
    messagebox.showinfo("About", "App with python and tkinter, that is a simple CRUD with sqlite3.\n                                         Heathens Inc @2021")

