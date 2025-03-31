def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

cislo = int(input("Napiš číslo: "))
print(f"Faktoriál čísla {cislo} je {factorial(cislo)}")