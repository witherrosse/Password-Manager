from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import choice, randint, shuffle

def generate_password():

    ### Lists of characters to use in password ###

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ### Generate random number of each character type ###

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    ### Combine and shuffle all characters ###

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    ### Convert list to string ###

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    ### Get data from entry fields ###

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    ### Check if any field is empty ###

    if len(website) == 0 or len(email) == 0:
        messagebox.showerror("Oops", "Please do not leave any fields as empty")
    else:

        ### Ask user to confirm saving ###

        messagebox.askokcancel(title=website, message=f"These are the details of entered: \n Email: {email} "
                                                      f"\nPassword: {password}\n is it ok to save ?")

        try:

            ### Try to open existing JSON file ###

            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:

            ### Create new file if it doesn't exist ###

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            ### Update existing data with new entry ###

            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            ### Clear entry fields after saving ###

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------- Search Website ------------------------------ #

def find_password():

    ### Search for website in JSON file ###

    website = website_entry.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            show_up_message = data[website]
        except KeyError:
            messagebox.showerror("Oops", "Sorry, the website does not exist")
        else:
            messagebox.showinfo(title=website, message=f" Email: {show_up_message['email']}\n Password: "
                                                       f"{show_up_message['password']}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

### Logo image ###

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

### Labels ###

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

### Entry fields ###

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()   # Start cursor here

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "alifooladi.me.wither@gmail.com")   # Default email

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

### Buttons ###

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()