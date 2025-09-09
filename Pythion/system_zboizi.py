import tkinter as tk

#okno
window = tk.Tk()
window.title("Tabulka skladu") # Název
window.minsize(width=900, height=900)
window.maxsize(width=1950, height=1020)
window.config(bg="#696969")


#funkce
print("Seznam zboží")
a = input("Zboží: ")
b = input("datum_trvanlosti: ")
c = int(input("počet kusů: "))
d = int(input("počet krabic: "))
 
print(a, b, str(c * d) + "x")

#Hlavní cyklus okna
window.mainloop()