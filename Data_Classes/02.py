from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name: str
    age: int

    def __str__(self) -> str:
        return self.name

p1 = Person(21, 'mohamed')
p2 = Person(23,'Ali')

print(p1 > p2)