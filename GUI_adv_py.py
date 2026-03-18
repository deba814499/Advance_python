from tkinter import *
from tkinter import messagebox

# Main Window
root = Tk()
root.title("GIETU Student Registration Form")
root.geometry("700x600")
root.config(bg="#2c3e50")

# Title
title = Label(root,
              text="GIETU Student Registration Form",
              font=("Arial",20,"bold"),
              bg="#2c3e50",
              fg="white")
title.pack(pady=10)

# Frame for form
frame = Frame(root,bg="#ecf0f1",bd=5,relief=RIDGE)
frame.place(x=80,y=80,width=540,height=430)

# Functions
def submit_data():

    info = f"""
Student Details

Roll No : {roll_entry.get()}
Name : {name_entry.get()}
Department : {dept_var.get()}
Gender : {gender_var.get()}
Address : {address_text.get("1.0",END)}
"""

    messagebox.showinfo("Student Data Submitted",info)


def clear_data():

    roll_entry.delete(0,END)
    name_entry.delete(0,END)
    dept_var.set("Select")
    gender_var.set("")
    address_text.delete("1.0",END)


# Roll No
roll_label = Label(frame,text="Roll No",font=("Arial",12),bg="#ecf0f1")
roll_label.grid(row=0,column=0,padx=10,pady=10)

roll_entry = Entry(frame,font=("Arial",12))
roll_entry.grid(row=0,column=1,padx=10,pady=10)

# Name
name_label = Label(frame,text="Name",font=("Arial",12),bg="#ecf0f1")
name_label.grid(row=1,column=0,padx=10,pady=10)

name_entry = Entry(frame,font=("Arial",12))
name_entry.grid(row=1,column=1,padx=10,pady=10)

# Department
dept_label = Label(frame,text="Department",font=("Arial",12),bg="#ecf0f1")
dept_label.grid(row=2,column=0,padx=10,pady=10)

dept_var = StringVar()
dept_var.set("Select")

dept_menu = OptionMenu(frame,dept_var,
                       "CSE",
                       "ECE",
                       "EEE",
                       "Mechanical",
                       "Civil")
dept_menu.grid(row=2,column=1,padx=10,pady=10)

# Gender
gender_label = Label(frame,text="Gender",font=("Arial",12),bg="#ecf0f1")
gender_label.grid(row=3,column=0,padx=10,pady=10)

gender_var = StringVar()

male = Radiobutton(frame,text="Male",
                   variable=gender_var,
                   value="Male",
                   bg="#ecf0f1")

female = Radiobutton(frame,text="Female",
                     variable=gender_var,
                     value="Female",
                     bg="#ecf0f1")

male.grid(row=3,column=1,sticky="w")
female.grid(row=3,column=1,sticky="e")

# Address
address_label = Label(frame,text="Address",font=("Arial",12),bg="#ecf0f1")
address_label.grid(row=4,column=0,padx=10,pady=10)

address_text = Text(frame,width=25,height=4)
address_text.grid(row=4,column=1,padx=10,pady=10)

# Buttons
submit_btn = Button(frame,
                    text="Submit",
                    font=("Arial",12,"bold"),
                    bg="#27ae60",
                    fg="white",
                    command=submit_data)

submit_btn.grid(row=5,column=0,pady=20)

clear_btn = Button(frame,
                   text="Clear",
                   font=("Arial",12,"bold"),
                   bg="#e67e22",
                   fg="white",
                   command=clear_data)

clear_btn.grid(row=5,column=1,pady=20)

exit_btn = Button(frame,
                  text="Exit",
                  font=("Arial",12,"bold"),
                  bg="#c0392b",
                  fg="white",
                  command=root.destroy)

exit_btn.grid(row=6,column=0,columnspan=2,pady=10)

root.mainloop()