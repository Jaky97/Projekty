import tkinter

#okno
window = tkinter.Tk()
window.title("Menu")
window.minsize(width=900, height=900)
window.maxsize(width=1950, height=1020)
window.config(bg="#0e0e8c")

#text
label_text = tkinter.Label(window, text="Vyberte možnost", font=("Arial", 30), fg="#00BFFF", bg="#0e0e8c")
label_text.grid(row=0, column=0, pady=20)  # Umístění textu

# Přizpůsobení mřížky
window.grid_rowconfigure(0, weight=0)  # Umožní růst prvního řádku
window.grid_rowconfigure(3, weight=1)  # Pro tlačítka
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)  # Umožní centrování

# Funkce pro tlačítka
def tlacitko():
    #okno
    window = tkinter.Tk()
    window.title("XP Staty")
    window.minsize(width=900, height=900)
    window.maxsize(width=1950, height=1020)
    window.config(bg="#0e0e8c")

def tlacitko_2():
        #okno
    window = tkinter.Tk()
    window.title("Aktuální Level")
    window.minsize(width=900, height=900)
    window.maxsize(width=1950, height=1020)
    window.config(bg="#0e0e8c")

def tlacitko_3():
        #okno
    window = tkinter.Tk()
    window.title("Quests")
    window.minsize(width=900, height=900)
    window.maxsize(width=1950, height=1020)
    window.config(bg="#0e0e8c")

# tlačítka
button1 = tkinter.Button(window, text="XP staty", font=("Arial", 20), fg="#00BFFF", bg="#0000CD", command=tlacitko)
button1.grid(row=1, column=0, pady=10)  # Správné umístění

button2 = tkinter.Button(window, text="Aktuální Level", font=("Arial", 20), fg="#00BFFF", bg="#0000CD", command=tlacitko_2)
button2.grid(row=2, column=0, pady=10, sticky="n")

button3 = tkinter.Button(window, text="Quests", font=("Arial", 20), fg="#00BFFF", bg="#0000CD", command=tlacitko_3)
button3.grid(row=3, column=0, pady=10, sticky="n")

#Hlavní cyklus
window.mainloop()