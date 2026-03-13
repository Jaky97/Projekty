import random

status = 8
ustatus = True
lstatus = True
nstatus = True
sstatus = True
#seznamy
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/' ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
password = []

#Hlavní cyklus
while True:

    print("|    Password Generator    |")
    print("|       1. Generate        |")
    print("|       2. Settings        |")
    print("|       3. Exit            |")

    choice = input("Select an option: ")
    if choice == "1":
        print("Generating...\n")
        for i in range(status):
            character = random.randrange(0,4)
            if character == 0:
                password.append(random.choice(lowercase))
            elif character == 1:
                password.append(random.choice(uppercase))
            elif character == 2:
                password.append(random.choice(numbers))
            elif character == 3:
                password.append(random.choice(special))
            else:
                print("error pičo")
            
        print(password.join())

    elif choice == "2":
        print("\n|          Settings                 |")
        print("|    1. Change length             " + str(status) + " |")
        print("|    2. Upper case characters  " + str(ustatus) + " |")
        print("|    3. Lower case characters  " + str(lstatus) + " |")
        print("|    4. Numbers                " + str(nstatus) + " |")
        print("|    5. Special characters     " + str(sstatus) + " |")
        print("|    6. Back                        |\n")
        choice2 = input("Select an option: ")
        if choice2 == "1":
            status = int(input("Enter new length: "))
            print(status)
        elif choice2 == "2":
            ustatus = input("Type True or False: ")
            print(ustatus)
        elif choice2 == "3":
            lstatus = int(input("Type True or False: "))
            print(lstatus)
        elif choice2 == "4":
            nstatus = int(input("Type True or False: "))
            print(nstatus)
        elif choice2 == "5":
            sstatus = int(input("Type True or False: "))
            print(sstatus)
        elif choice2 == "6":
            continue
        else:
            print("ZEDEJ ČÍSLO!!!!!!\n")

    elif choice == "3":
        print("Exiting...\n")
        break
    else:
        print("ZEDEJ ČÍSLO!!!!!!\n")