class Projektor:
    def zapnout(self):
        print("Projektor: Zapínám se...")
    def vypnout(self):
        print("Projektor: Vypínám se...")
    def nastavit_vstup_hdmi(self):
        print("Projektor: Přepínám vstup na HDMI.")

class Reproduktory:
    def zapnout(self):
        print("Reproduktory: Zapínám napájení...")
    def vypnout(self):
        print("Reproduktory: Vypínám napájení...")
    def nastavit_hlasitost(self, hodnota):
        print(f"Reproduktory: Nastavuji hlasitost na úroveň {hodnota}.")

class Platno:
    def spustit_dolu(self):
        print("Plátno: Sjíždím dolů.")
    def vytahnout_nahoru(self):
        print("Plátno: Roluji nahoru.")


# --- FASÁDA ---

class ProjektorovySystem:
    def __init__(self):
        # Fasáda zapouzdřuje instance subsystémů
        self.projektor = Projektor()
        self.reproduktory = Reproduktory()
        self.platno = Platno()

    def zapnout_prezentaci(self):
        print("\n--- Spouštím prezentační mód ---")
        self.platno.spustit_dolu()
        self.projektor.zapnout()
        self.projektor.nastavit_vstup_hdmi()
        self.reproduktory.zapnout()
        self.reproduktory.nastavit_hlasitost(20)
        print("--- Systém je připraven ---\n")

    def vypnout_prezentaci(self):
        print("\n--- Ukončuji prezentaci ---")
        self.projektor.vypnout()
        self.reproduktory.vypnout()
        self.platno.vytahnout_nahoru()
        print("--- Vše bezpečně vypnuto ---\n")

if __name__ == "__main__":
    system = ProjektorovySystem()
    # Učitel ovládá celý systém jedním příkazem
    system.zapnout_prezentaci()
    system.vypnout_prezentaci()