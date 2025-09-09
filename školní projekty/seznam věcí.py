# Vytvoření seznamu
muj_seznam = ["jablko", "hruška", "banán"]

# Změna hodnoty na indexu 0
muj_seznam[0] = "meloun"
print("Po změně indexu 0:", muj_seznam)  # Vypíše: ['meloun', 'hruška', 'banán']

# Změna hodnoty na indexu 2
muj_seznam[2] = 123
print("Po změně indexu 2:", muj_seznam)  # Vypíše: ['meloun', 'hruška', 123]

# Vložení nového prvku na index 1
muj_seznam.insert(1, "kiwi")
print("Po vložení na index 1:", muj_seznam)  # Vypíše: ['meloun', 'kiwi', 'hruška', 123]