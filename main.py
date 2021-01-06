from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint,shuffle,choice

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)

def password_generator():
    password_entry.delete(0,END)
    letters_list = [choice(letters) for letter in range(nr_letters)]
    symbols_list = [choice(symbols) for symbol in range(nr_symbols)]
    numbers_list = [choice(numbers) for number in range(nr_numbers)]

    password_list = letters_list+symbols_list+numbers_list

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
    messagebox.showinfo(title="Password saved to clipboard", message="Your password has been saved to the clipboard, ready for pasting")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showerror(title="Please fill out all inputs", message="You missed out on at least one field, please ensure form is filled out")
        pass

    elif len(password) < 1:
        messagebox.showerror(title="Password not generated", message="Please click 'Generate Password' ")
    else:
        with open(f"./passwordlist.txt", mode="a") as password_save :
            password_save.write(f"{website} | {email} | {password}\n")
            messagebox.showinfo(title="Password Saved", message=f"Your password for {email} on {website} has been saved")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20, bg="white")

canvas = Canvas(width=200,height=200, bg="white")

padlock = PhotoImage(file="logo.png",width=200)
canvas.create_image(100,100,image=padlock)
canvas.grid(column=1,row=1)

website_label = Label(text="Website")
website_label.grid(column=0,row=2)
website_entry = Entry(text="", width=35)
website_entry.focus()
website_entry.grid(column =1, row=2, columnspan=2)

email_label = Label(text="Email / Username")
email_label.grid(column=0,row=3)
email_entry = Entry(text="", width=35)
email_entry.grid(column =1, row=3, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0,row=4)
password_entry = Entry(text="", width=21)
password_entry.grid(column =1, row=4, columnspan=1)
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1,row=5, columnspan=2)
window.mainloop()