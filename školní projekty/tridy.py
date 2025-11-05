class tridy:
    count = 0
    chlapci = 0
    divky = 0
    celkem_zaku = 0

    def __init__(self, divky, chlapci, celkem):
        self.divky = divky
        self.chlapci = chlapci
        self.celkem = celkem
        tridy.count += 1
        tridy.chlapci += chlapci
        tridy.divky += divky
        tridy.celkem_zaku += celkem
    def __del__(self):
        tridy.count -= 1
        tridy.chlapci -= self.chlapci
        tridy.divky -= self.divky
        tridy.celkem_zaku -= self.celkem


A1 = tridy(11, 12, 23)
B1 = tridy(12, 13, 25)
C1 = tridy(8, 10, 18)
A2 = tridy(13, 8, 21)
B2 = tridy(13, 12, 25)
C2 = tridy(12, 10, 22)

print(tridy.divky)
print(tridy.chlapci)
print(tridy.celkem_zaku)
print(tridy.count)

print(A1.divky)
print(B2.chlapci)
print(C1.celkem)
del A1
print(tridy.divky)
print(tridy.chlapci)
print(tridy.celkem_zaku)
print(tridy.count)