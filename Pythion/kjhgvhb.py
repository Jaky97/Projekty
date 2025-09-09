import tkinter
import json
import os

# Application window
window = tkinter.Tk()
window.title("Rybářské Potřeby Holátko")
window.minsize(width=700, height=600)
window.config(bg="#5ffee8")

def show_login_screen():
    main_frame.pack_forget()
    login_frame = tkinter.Frame(window, bg="#5ffee8")
    login_frame.pack(expand=True, fill="both")
    label_username = tkinter.Label(login_frame, text="Uživatelské jméno:", font=("Arial", 20), bg="#5ffee8")
    label_username.pack(pady=10)
    entry_username = tkinter.Entry(login_frame, font=("Arial", 20))
    entry_username.pack(pady=10)
    label_password = tkinter.Label(login_frame, text="Heslo:", font=("Arial", 20), bg="#5ffee8")
    label_password.pack(pady=10)
    entry_password = tkinter.Entry(login_frame, font=("Arial", 20), show="*")
    entry_password.pack(pady=10)
    button_back = tkinter.Button(login_frame, text="Zpět", font=("Arial", 20), command=lambda: back_to_main(login_frame))
    button_back.pack(pady=10)
    button_login = tkinter.Button(login_frame, text="Přihlásit se", font=("Arial", 20), command=lambda: login(entry_username.get(), entry_password.get()))
    button_login.pack(pady=10)

def show_signup_screen():
    main_frame.pack_forget()
    signup_frame = tkinter.Frame(window, bg="#5ffee8")
    signup_frame.pack(expand=True, fill="both")
    label_email = tkinter.Label(signup_frame, text="E-mail:", font=("Arial", 20), bg="#5ffee8")
    label_email.pack(pady=10)
    entry_email = tkinter.Entry(signup_frame, font=("Arial", 20))
    entry_email.pack(pady=10)
    label_new_username = tkinter.Label(signup_frame, text="Uživatelské jméno:", font=("Arial", 20), bg="#5ffee8")
    label_new_username.pack(pady=10)
    entry_new_username = tkinter.Entry(signup_frame, font=("Arial", 20))
    entry_new_username.pack(pady=10)
    label_new_password = tkinter.Label(signup_frame, text="Heslo:", font=("Arial", 20), bg="#5ffee8")
    label_new_password.pack(pady=10)
    entry_new_password = tkinter.Entry(signup_frame, font=("Arial", 20), show="*")
    entry_new_password.pack(pady=10)
    button_back = tkinter.Button(signup_frame, text="Zpět", font=("Arial", 20), command=lambda: back_to_main(signup_frame))
    button_back.pack(pady=10)
    button_continue = tkinter.Button(signup_frame, text="Pokračovat", font=("Arial", 20), command=lambda: continue_signup(entry_email.get(), entry_new_username.get(), entry_new_password.get()))
    button_continue.pack(pady=10)

# Funkce pro návrat do hlavního menu
def back_to_main(current_frame):
    current_frame.pack_forget()
    main_frame.pack(expand=True, fill="both")

# Main Frame
main_frame = tkinter.Frame(window, bg="#5ffee8")
main_frame.pack(expand=True, fill="both")

# Inner Frame for buttons (to center them vertically)
button_frame = tkinter.Frame(main_frame, bg="#5ffee8")
button_frame.pack(expand=True)  # Center the button frame vertically

# Buttons
# Login button
buton_m_login = tkinter.Button(button_frame, text="Přihlásit se", font=("Arial", 20), fg="#000000", command=show_login_screen)
buton_m_login.pack(pady=10, padx=40)
# Signup button
button_m_signup = tkinter.Button(button_frame, text="Zaregistrovat se", font=("Arial", 20), fg="#000000", command=show_signup_screen)
button_m_signup.pack(pady=10, padx=40)
# Exit button
button_m_exit = tkinter.Button(button_frame, text="Konec", font=("Arial", 20), fg="#000000", command=window.quit)
button_m_exit.pack(pady=10, padx=10)

# Main cycle
window.mainloop()