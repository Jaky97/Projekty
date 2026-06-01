#Data 
data = [
    {'name': 'Anna', 'age': 19, 'score': 85},
    {'name': 'Petr', 'age': 17, 'score': 60},
    {'name': 'Eva', 'age': 21, 'score': 92},
    {'name': 'Jan', 'age': 18, 'score': 70},
    {'name': 'Lucie', 'age': 20, 'score': 88}
]

#Mam to tu malo barevný :(

class Query:
    def __init__(self, data):
        self.data = data

    def execute(self):
        return self.data
    
#seřazení od nejmladšího po nejstarší
    def sort_by(self, field, descending=False):
        self.data.sort(key=lambda x: x[field], reverse=descending)
        return self
    
#kolik lidí to muže max napsat
    def limit(self, count):
        self.data = self.data[:count]
        return self
    
#Od < > = porovnání 
    def filter(self, field, operator, value):
        result = []
        for item in self.data:
            if operator == ">":
                if item[field] > value:
                    result.append(item)
            elif operator == "<":
                if item[field] < value:
                    result.append(item)
            elif operator == "=":
                if item[field] == value:
                    result.append(item)
        self.data = result

        return self
#třídí přeskakuje opakující se lidi podle zadaného parametru
    def distinct(self, field):
        seen = []
        result = []
        for item in self.data:
            if item[field] not in seen:
                seen.append(item[field])
                result.append(item)
        self.data = result

        return self
#Konec tady to píše výsledek        
result = Query(data).sort_by("age").limit(3).filter("age", ">", 18).distinct("age").execute()
print(result)