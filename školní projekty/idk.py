class dog:

    count = 0
    suma = 0

    def __init__(self, race, sex, age, price):
        self.race = race
        self.sex = sex
        self.age = age
        self.price = price
        dog.count += 1
    def __del__(self):
            dog.count -= 1
            dog.suma += self.price


print(dog.count)
shiba_inu = dog("Shiba Inu", "M", 1, 15000)
shiba_tzu = dog("Shih Tzu", "F", 2, 10000)
bulldog = dog("Bulldog", "M", 3, 20000)
husky = dog("Husky", "F", 2, 18000)

print(dog.count)
del shiba_inu
del shiba_tzu
print(dog.count)
print(dog.suma)
    