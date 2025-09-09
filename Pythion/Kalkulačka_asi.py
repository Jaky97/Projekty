def pocet(pocet = 0):
    a = float(input("čislo A: "))
    cc = input("Znamenko (+ ,- ,* ,/): ")
    b = float(input("čislo B: "))

    if cc == "/" and (a == 0 or b == 0):
        print("Nejde dělit nulou!")
    else:
        if cc == "+":
            print(a + b)
        elif cc == "-":
            print(a - b)
        elif cc == "*":
            print(a * b)
        else:
            print(a / b)
pocet()