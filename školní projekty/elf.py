class otroci:
    pocet_elfu = 0

    def __init__(self, jmeno, vyrobek):
        self.jmeno = jmeno
        self.vyrobek = vyrobek
        otroci.pocet_elfu += 1
    def __del__(self):
        otroci.pocet_elfu -= 1

e1 = otroci("Elrond", "plyšovích medvídcích")
e2 = otroci("Boris", "panenkách")
e3 = otroci("Vladimir", "uhelném dole")
e4 = otroci("Lina", "autíčkách")

print("V dílně pracují " + str(otroci.pocet_elfu) + " elfové.")
print("Elf "+ e1.jmeno + " pracuje na " + e1.vyrobek)
print("Elf "+ e2.jmeno + " pracuje na " + e2.vyrobek)
print("Elf "+ e3.jmeno + " pracuje na " + e3.vyrobek)
print("Elf "+ e4.jmeno + " pracuje na " + e4.vyrobek)

print("Zaměstnanec " + e2.jmeno + " byl eliminován. Duvod: pokus o útěk z tabora.")
del e2
print("V dílně pracují " + str(otroci.pocet_elfu) + " elfové.")