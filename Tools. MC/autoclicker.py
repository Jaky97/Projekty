import time
import mouse
import keyboard

status = False

while True:
    print("|   Controls   |")
    print("|   1. Start   |")
    print("|   2. Guide   |")
    print("|   3. Exit    |")
    action = str(input("Zadej číslo akce: "))
    if action == "1":
        print("\n""\n")
#timer and autoclicker
        speed = float(input("Zadej rychlost v sekundách: "))
        seconds = 5
        for i in range(seconds, 0, -1):
            if i == 1:
                print(f"{0} sekunda zbývá...")
                print("Zastav pomocí klávesy 'o'")
            else:
                print(f"{i} sekund zbývá...", end="\r")
            time.sleep(1)
        print("Spouštím autoclicker...")
        status = True
        while status == True:
            if keyboard.is_pressed("o"):
                print("Autoclicker zastaven.")
                status = False
                print("\n""\n")
                break
            else:
                mouse.click(button="left")
                time.sleep(speed)

    elif action == "2":
        print("|                             Guide                              |")
        print("|  Zadej rychlost v sekundách. '1's pro menší čísla zadej '0.1's |")
        print("|  Po zadání čísla se spustí 5s časovač pro přesun kurzoru       |")
        print("|  Pro ukončení stisni klávesu 'o'                               |")
        print("\n""\n")

    elif action == "3":
        print("Exit")
        break

    else:
        print("Try Again")
        print("\n""\n")