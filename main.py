from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
img = 'logo.png'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    passwd.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    website = webTx.get()
    emailid = email.get()
    password = passwd.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="OOPS", message="One of the Website or Password field is empty. Please check again!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enetered:\nEmail: {emailid}\n Password: {password}\nIs this ok to save??\n")

        if is_ok:
            out = f"{website}|{emailid}|{password}"
            with open("out.txt", "a") as f:
                f.write(f"{out}\n")

            webTx.delete(0, 'end')
            passwd.delete(0, 'end')
            webTx.focus()
        else:
            webTx.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
bgImg = PhotoImage(file=img)
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bgImg)
canvas.grid(row=0, column=1)

#Labels
web = Label(text="Website:")
web.grid(row=1, column=0)
mail = Label(text="Email/Username:")
mail.grid(row=2, column=0)
passw = Label(text="Password:")
passw.grid(row=3, column=0)

#Entry
webTx = Entry(width=36)
webTx.focus()
webTx.grid(row=1, column=1, columnspan=2)
email = Entry(width=36)
email.insert(0, "noddy@amazon.com")
email.grid(row=2, column=1, columnspan=2)
passwd = Entry(width=21)
passwd.grid(row=3, column=1)

#Button
generate = Button(text="Generate Password", command=gen_pass)
generate.grid(row=3, column=2)
add = Button(text="Add", width=36, command=get_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()