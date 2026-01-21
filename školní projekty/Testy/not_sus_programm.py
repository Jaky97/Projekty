import tkinter
import webbrowser

#okno
window = tkinter.Tk()
window.title("Comand Prompt")
window.config(bg="#000000")
window.minsize(width=500, height=300)

#text
txt = tkinter.Text(window, bg="#000000", fg="#00ff41", font=("Consolas", 10))
txt.pack(padx=10, pady=(0,10), fill='both', expand=True,)
txt.config(state='disabled', relief="flat")

#krade text
def add_text():
    text = entry.get().strip()          
    if not text:                        # pokud je prázdné → nic
        return

    if text.lower() == "help":
        txt.insert('end', "Otevírám nápovědu...\n")
        
        # rickroll 5× po sobě
        rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        advertisement = "https://www.instagram.com/redbluefoxstudios"
        advertisement2 = "https://www.instagram.com/cozyfox_rbf"
        for _ in range(5):
            webbrowser.open_new(rickroll_url)
        for _ in range(2):
            webbrowser.open_new(advertisement)
            webbrowser.open_new(advertisement2)
        
        txt.insert('end', "Nápověda byla úspěšně doručena 5×!\n")
    else:
        txt.insert('end', "Neznámý příkaz. Zkus 'help'\n")

    txt.config(state='normal')         
    txt.insert('end', "C:\\Users\\kozak> <type help for more info> " + text + '\n')      # přidat na konec + nový řádek
    txt.config(state='disabled')       
    txt.see('end')                      

    entry.delete(0, 'end')

#psací řádek
entry = tkinter.Entry(window)
entry.pack(pady=10, fill='x', padx=10)
entry.config(bg="#000000", fg="#00FF00", insertbackground="#00FF00", font=("Consolas", 10),relief="flat")

entry.bind('<Return>', lambda event: add_text())
entry.focus()
window.mainloop()