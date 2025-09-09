print("Ceník:\n dětská……85\n dospělá…150\n senior…70")
d = float(input("Počet dětských vstupenek: "))
do = float(input("Počet dospělích vstupenek: "))
se = float(input("Počet vstupenek pro seniory: "))
price = (d*85 + do*150 + se*70)
if price > 1000:
    price = (price * 0.8)
    print(str(price) + " Kč")
else:print(str(price) + " Kč")