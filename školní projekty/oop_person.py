
#konstruktor
class Lady:
    def __init__(self, h, w, a, sex, status, skin):
        self.height = hasattr
        self.weight = w 
        self.age = a 
        self.sex = sex 
        self.status = status
        self.skin = skin
    
    def about(self):
        S = "Hi!" + "I am " + str(self.age) + " years old, " + "I am " + self.status + "now. Would you like to date me?"
        return S
black_lady = Lady(165, 55, 17, "f", "single ", "black")
white_lady = Lady(170, 60, 18, "f", "married ", "white") 
gray_lady = Lady(160, 50, 19, "f", "dead ", "gray")


print(black_lady.status)
print(white_lady.status)
print(gray_lady.status)

print(black_lady.about())
print(white_lady.about())
print(gray_lady.about())

class Vehicle:
    def __init__(self, model, speed, horse_power):
        self.model = model
        self.speed = speed
        self.horse_power = horse_power

    def drive(self, driver):
        return driver + "drive this vehicle."
    
    def crash(self, driver):
        return  self.model + "crashed by" + driver
    
bmw = Vehicle("BMW X6", 250, 200)
print(bmw.drive(" Adela "))
print(bmw.crash(" Adela "))

class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def about(self):
        B = "Name of this book is " + self.title + " and it is written by " + self.author + ". It have " + str(self.pages) + " pages."
        return B
    def read(self, reader):
        return reader + "reads " + self.title

book1 = book("Harry Potter", "J.K. Rowling", 300)
book2 = book("Lord of the Rings", "J.R.R. Tolkien", 1472)
book3 = book("Hobit", "J.R.R. Tolkien", 200)
book4 = book("Bible", "Vatican", 1392)

print(book1.about())
print(book1.read("Pepa "))
print(book2.about())
print(book2.read("Aneta "))
print(book3.about())
print(book3.read("Saša "))
print(book4.about())
print(book4.read("Michal "))