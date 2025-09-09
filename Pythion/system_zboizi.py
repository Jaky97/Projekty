import tkinter as tk

#window
window = tk.Tk()
window.title("Tabulka skladu") # Název
window.minsize(width=900, height=900)
window.maxsize(width=1950, height=1020)
window.config(bg="#696969")

#Lists of things
zbozi = []
datum = []
ks = []
box = []
all_ks = []

#function
print("Seznam zboží")
a = input("Zboží: ")
b = input("datum_trvanlosti: ")
c = int(input("počet ks v krabici: "))
d = int(input("počet krabic: "))

#Add to Lists of things
zbozi.insert(0, a)
datum.insert(0, b)
ks.insert(0, c)
box.insert(0, d)
all_ks.insert(0, c*d)

#print in terminal name of list and inside of it
print('Zboží: ',zbozi)
print('Datum:', datum)
print('Kusy:', ks)
print('Krabice:', box)
print('Celkem ks:', all_ks)

#Cycle that keep window open
window.mainloop()