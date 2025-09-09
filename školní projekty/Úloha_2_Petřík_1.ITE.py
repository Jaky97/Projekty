n = int(input("Zadej počet členů n: "))
a1 = int(input("Zadej prvního člena a1: "))
d = int(input("Zadej přírůstek d: "))

for i in range(1, n + 1):
    print(("a" + str(i) + "=") + str(a1 + (i - 1) * d))