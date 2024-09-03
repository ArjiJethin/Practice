class Person:
    def __init__(self, name):
        self.name = name


user_input = input("Enter your name: ")

person = Person(user_input)
print("Name: ", person.name)