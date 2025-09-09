import tkinter
import json
import os

# File to store the data
DATA_FILE = "people_data.json"

# Funkce pro načtení dat z JSON souboru
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Funkce pro uložení dat do JSON souboru
def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

# Funkce pro přihlášení
def login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()
    
    # Načtení seznamu uživatelů
    users = load_users()
    
    # Kontrola, zda uživatel existuje
    for user in users:
        if user["name"] == entered_username:
            # Pokud heslo ještě není nastaveno, můžeme ho přidat
            if "password" not in user or user["password"] == entered_password:
                if "password" not in user and entered_password:
                    user["password"] = entered_password
                    save_users(users)  # Uložit nové heslo do souboru
                result_label.config(text=f"Přihlášení úspěšné: {entered_username}", fg="green")
                return
            else:
                result_label.config(text="Špatné heslo!", fg="red")
                return
    
    result_label.config(text="Uživatel nenalezen!", fg="red")

# Okno
window = tkinter.Tk()
window.title("Přihlašovací okno")
window.minsize(width=350, height=500)
window.maxsize(width=400, height=500)

# Popisek a pole pro uživatelské jméno
label_username = tkinter.Label(window, text="Uživatelské jméno:")
label_username.pack(pady=10)
entry_username = tkinter.Entry(window)
entry_username.pack(pady=5)

# Popisek a pole pro heslo
label_password = tkinter.Label(window, text="Heslo:")
label_password.pack(pady=10)
entry_password = tkinter.Entry(window, show="*")
entry_password.pack(pady=5)

# Tlačítko pro přihlášení
button_login = tkinter.Button(window, text="Přihlásit se", command=login)
button_login.pack(pady=20)

# Popisek pro výsledek přihlášení
result_label = tkinter.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Hlavní cyklus
window.mainloop()