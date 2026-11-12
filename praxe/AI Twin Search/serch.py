import tkinter
from tkinter import *
from tkinter import ttk


window = tkinter.Tk()
window.title("Search Your Self")
window.title
window.minsize(width=900, height=600)
window.maxsize(width=1950, height=1020)
window.config(bg="#860907")
frm = ttk.Frame(window, padding=10)
frm.grid()

ttk.Label(frm, text="Zadej svoje osobní udaje.").grid(column=4, row=0)
ttk.Button(frm, text="Odejdi Prosím", command=window.destroy).grid(column=30, row=30)


window.mainloop()