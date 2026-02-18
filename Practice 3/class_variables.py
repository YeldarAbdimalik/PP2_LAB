class Person:
    species = "Human"   # Class variable

    def __init__(self, name):
        self.name = name   # Instance variable

p1 = Person("Alice")
p2 = Person("Bob")

print(p1.species)
print(p2.species)
