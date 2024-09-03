class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


sammi = Dog("Sammi", "Husky")
casey = Dog("Casey", "Chocolate Lab")

print(f"{sammi.name} is a {sammi.breed} - {Dog.species}")
print(f"{casey.name} is a {casey.breed} - {Dog.species}")
