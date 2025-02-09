'''Problem: Animal Sounds
    You need to create a program that simulates different types of animals making sounds.
    Each animal will have a name and a specific sound it makes.
    You should be able to create different animals(like dogs, cats, cows)
    and have them "speak."
'''

class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal): 
       def speak(self):
        print(f" {self.name} says woof!")

class Cat(Animal): 
       def speak(self):
        print(f" {self.name} says nyan!")

class Cow(Animal): 
       def speak(self):
        print(f" {self.name} says Moo!")
# Create instances of each animal



dog = Dog("Buddy")
cat = Cat("Kitty")
cow = Cow("Daisy")

dog.speak()