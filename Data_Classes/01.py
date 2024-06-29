

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age =age


    def __str__(self):
        return (f'Person = ( name -{self.name} , age - {self.age})')
    
    def __gt__(self, other):
        return self.age > other.age
    

    def __lt__(self, other):
        return self.age < other.age
    




p1 = Person('mohamed', 21)
p2 = Person('Ali', 23)
print(p1)
print(p1.name)
print(p1.age)


print(p1 > p2)