## Password Manager - How it works

This is a **secure password manager app** built with Tkinter. It generates strong passwords, saves website login details, and allows you to search for saved passwords.

### Project files

- `main.py` – the complete application
- `logo.png` – app logo image
- `data.json` – stores all saved passwords (created automatically)

### What is used

- `tkinter` module: for GUI window, labels, entries, and buttons
- `json` module: to save and load password data
- `messagebox`: for pop-up alerts and confirmations
- `random` module: to generate random passwords

### How it works

**1. Generate a password**
- Click "Generate Password" button
- Creates a random password with 8-10 letters, 8-10 numbers, and 2-4 symbols
- Password appears automatically in the password field

**2. Save website details**
- Enter website name, email, and password (or generate one)
- Click "Add" button
- App asks for confirmation
- Saves data to `data.json` file
- Clears website and password fields automatically

**3. Search for saved password**
- Enter website name
- Click "Search" button
- Shows email and password for that website if found
- Shows error message if website not found

### Features

- Strong random password generator
- Data saved permanently in JSON format
- Search functionality to find old passwords
- Empty field validation
- Confirmation before saving

### File structure

```
Project/
├── main.py
├── logo.png
└── data.json    (created after first save)
```

### JSON data format

```json
{
    "google": {
        "email": "user@gmail.com",
        "password": "aB3$dF9#"
    },
    "facebook": {
        "email": "user@gmail.com",
        "password": "Xy2&kL7@"
    }
}
```

### Buttons explained

| Button | Action |
|--------|--------|
| Generate Password | Creates random strong password |
| Search | Finds saved password for a website |
| Add | Saves website login details |

---

