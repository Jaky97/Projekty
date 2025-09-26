#FirstName: Lastname: Ranking: Price_Money:
def businesscard(**person):
    print(f"{person['firstname']} {person['lastname']} is ranked {person['ranking']} and has won ${person['pricemoney']} so far this year.")

businesscard(firstname = "Franta", lastname = "Dvořák", ranking = "2" , pricemoney = "5000")
