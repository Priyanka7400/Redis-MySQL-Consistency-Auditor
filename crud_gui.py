from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@4411",
        database="auditdb"
    )
def insert():
    con = connect_db()
    cur = con.cursor()

    sql="INSERT INTO users(id,name,age,city) VALUES (%s,%s,%s,%s)"
    values=(id_entry.get(),
         name_entry.get(),
         age_entry.get(),
         city_entry.get())
    cur.execute(sql,values)
    con.commit()
    con.close()
    messagebox.showinfo("success","Record inserted")
    view_all()

def search():
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROME user WHERE id=%s",(id_entry.get(),))
    row = cur.fetchone()

    if row:
        name_entry.delete(0,END)
        age_entry.delete(0,END)
        city_entry.delete(0,END)

        name_entry.insert(0,row[1])
        age_entry.insert(0,row[2])
        city_entry.insert(0,row[3])
    else:
        messagebox.showinfo("Not Found","Record not Found")
    con.close()    
def update():
    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "UPDATE users SET name=%s, age=%s, city=%s WHERE id=%s",
        (name_entry.get(), age_entry.get(), city_entry.get(), id_entry.get())
    )

    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record Updated")
    view_all()


def delete():
    con = connect_db()
    cur = con.cursor()

    cur.execute("DELETE FROM users WHERE id=%s", (id_entry.get(),))

    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record Deleted")
    view_all()


def view_all():
    for row in tree.get_children():
        tree.delete(row)

    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM users")

    for row in cur.fetchall():
        tree.insert("", END, values=row)

    con.close()

root = Tk()
root.title("User Management System")
root.geometry("650x450")

Label(root, text="ID").grid(row=0, column=0,padx=5,pady=5)
id_entry=Entry(root)
id_entry.grid(row=0, column=1)

Label(root, text="Name").grid(row=1, column=0)
name_entry=Entry(root)
name_entry.grid(row=1, column=1)

Label(root, text="Age").grid(row=2, column=0)
age_entry=Entry(root)
age_entry.grid(row=2, column=1)

Label(root, text="City").grid(row=3, column=0)
city_entry=Entry(root)
city_entry.grid(row=3, column=1)

Button(root, text="Insert",command=insert).grid(row=4, column=0,pady=5)
Button(root, text="Search",command=search).grid(row=4, column=1)
Button(root, text="Update",command=update).grid(row=5, column=0)
Button(root, text="Delete",command=delete).grid(row=5, column=1)
Button(root, text="View All",command=view_all).grid(row=6, column=0)
tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "City"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

tree.column("ID", width=60)
tree.column("Name", width=120)
tree.column("Age", width=60)
tree.column("City", width=120)

tree.grid(row=7, column=0, columnspan=4, padx=10, pady=10)
view_all()
root.mainloop()