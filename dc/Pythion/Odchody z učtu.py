ucet = float(input("Zustatek na učtě: ")) #kolik peněz mam

while(ucet >= 0):
    odchod = float(input("zadej odchod z učtu: ")) #kolik peněz odejde z učtu

    #kontrola jestli učet nejde do negativu
    if (ucet - odchod) < 0:
        print("Tuto částku nejde vybrat!")
        break
    else:
        print("zustatek na uctu je: ")
        print(ucet - odchod)
        
        sz = input("Přeješ si pokračovat? Ano/Ne \n ").lower()
        if sz == "ano":
            continue
    
        elif sz== "ne":
            print("Dobře nashledanou")
            break
        else:
            print("Neplatná vloba.")
            continue