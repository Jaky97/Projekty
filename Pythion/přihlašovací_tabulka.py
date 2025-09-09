loginSignup = input("Login or Sign up\n").lower()
if loginSignup == "login":
    prihlaseni = input("Uživatel: ")
    heslo = input("Heslo: ")
elif loginSignup == "sign up":
    novyUzivatel = input("Jmeno: ")
    noveHeslo = input("Heslo: ")
    noveHeslo1 = input("Opakujte heslo: ")
    if noveHeslo1 != noveHeslo:
        print("Hesla se neshodují")
    else:
        print("Účet založen")
else:
    print("Neplatná vloba.")