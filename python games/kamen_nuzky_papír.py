import random
print("Hra kamen nuzky papir \n vyber 1.kamen, 2.nuzky nebo 3.papir")

ai = random.randint(1,3)
player = int(input("Zvol 1, 2 , 3: "))

if player == 1 and ai == 1:
    print(ai, player, "remiza")
elif player == 1 and ai == 2:
    print(ai, player, "vyhral jsi")
elif player == 1 and ai == 3:
    print(ai, player, "prohral jsi")
elif player == 2 and ai == 1:
    print(ai, player, "prohral jsi")
elif player == 2 and ai == 2:
    print(ai, player, "remiza")
elif player == 2 and ai == 3:
    print(ai, player, "vyhral jsi")
elif player == 3 and ai == 1:
    print(ai, player, "vyhral jsi")
elif player == 3 and ai == 2:
    print(ai, player, "prohral jsi")
elif player == 3 and ai == 3:
    print(ai, player, "remiza")