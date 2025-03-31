#program def součet vložit přirozené celé číslo nezáporné udělat součet všech čísel přes faktoriál 
#od 0 do n rekurzivně
def faktorial(n):
    if n == 0:
        return 1 
    elif n > 0:
        return n * faktorial(n - 1)

vstup = input("Zadejte nezáporné celé číslo: ")
if not vstup.isdigit() or int(vstup) < 0:
    print("Toto číslo neplatí")
else:
    cislo = int(vstup)
    print("Faktoriál čísla", cislo, "je", faktorial(cislo))
    