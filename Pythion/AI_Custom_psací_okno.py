import tkinter

# Okno
window = tkinter.Tk()
window.title("Přihlašovací okno")
window.minsize(width=350, height=500)
window.maxsize(width=400, height=500)

# Popisek pro uživatelské jméno
label_username = tkinter.Label(window, text="Uživatelské jméno:")
label_username.pack(pady=10)

# Textové pole pro uživatelské jméno
entry_username = tkinter.Entry(window)
entry_username.pack(pady=5)

# Textové pole pro heslo (skrývá text jako hvězdičky)
entry_password = tkinter.Entry(window, show="*")
entry_password.pack(pady=5)

# Funkce pro tlačítko (pro ukázku)
def login():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Uživatelské jméno: {username}, Heslo: {password}") #píše se do konzole

# Tlačítko pro přihlášení
button_login = tkinter.Button(window, text="Přihlásit se", command=login)
button_login.pack(pady=20)

# Hlavní cyklus
window.mainloop()