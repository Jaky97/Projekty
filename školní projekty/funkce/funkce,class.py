class Teacher:
    def __init__(self, fname, lname, nick, age, status, grade):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.age = age
        self.status = status
        self.grade = grade  

    def getInfo(self):
        return str(self.fname) + " " + str(self.lname) + ", " + str(self.grade)

sbor = {        
    "kozina" : Teacher("Petr", "Kozák", "Kozy", 52, "married", 1),
    "herman" : Teacher("Petr", "Heřmanský", "Pohádkoví_dědeček", 60, "Magic", 1),
    "ciril" : Teacher("Cyril", "Kochrda", "Test_lord", 52, "Infinite_papers", 4)
}

print(sbor["kozina"].fname)
print(sbor["herman"].status)
print(sbor["ciril"].nick)
print(sbor["kozina"].getInfo())