

class Food:

    def __init__(self, name):
        self.name = name
        print(f'Hello Food {self.name}')

class Eat(Food):
        def __init__(self, name, size):
            self.size = size
           
            super().__init__(name) # calling the parent class constructor

            print(f"{self.name}is eating and size is {self.size} ")    

class Drink(Eat):
    def __init__(self, name_drink, name, size):
        self.name_drink = name_drink

        super().__init__(name, size)
        print(f"{self.name_drink} is drinking and name ear is {self.name} and size is {self.size} ")


obj1 = Food('Pizza')
obj2 = Eat('Burger', 'Large')
obj3 = Drink('Coke', 'Water', 'Medium')
