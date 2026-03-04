class heater:
    def on(self, teplota):
        print("zapínám topení na teplotu " + str(teplota) + "°C")
    def off(self):
        print("vypínám topení")

class light:
    def on(self):
        print("zapínám světlo")
    def off(self):
        print("vypínám světlo")

class music:
    def on(self):
        print("zapínám hudbu")
    def off(self):
        print("vypínám hudbu")

#facade hlavní část nevim tu to prostě ovládá
class Dungedon:
    #interaguje s těma hore
    def __init__(self):
        self.heater = heater()
        self.light = light()
        self.music = music()

    #print help
    def help(self):
        print("|            Control comands           |\n""|1.Help - shows this message           |\n""|2.Noughty_time - starts room eqvipment|\n""|3.Over - turns off room eqvipment     |")
#on 
    def noughty_time(self, teplota):
        self.heater.on(teplota)
        self.light.on()
        self.music.on()
#off
    def over(self):
        self.heater.off()
        self.light.off()
        self.music.off()

#ovládání
dungedon = Dungedon()
dungedon.help()

while True:
    prikaz = input("\nZadej číslo příkazu (1-3) nebo 'exit': ").strip()

    if prikaz == "1":
        dungedon.help()
        
    elif prikaz == "2":
            t = int(input("Zadej teplotu pro topení: "))
            dungedon.noughty_time(t)
            
    elif prikaz == "3":
        dungedon.over()
        
        
    elif prikaz.lower() == "4":
        print("Ukončuji program...")
        break
        
    else:
        print("Neznámý příkaz, zkus to znovu. Zadej číslo")
