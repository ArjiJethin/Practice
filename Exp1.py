class Car:
    __auth_key = 345678663

    def __init__(self, name, model, key):
        self.name = name
        self.model = model
        self.key = key
        if self.key == Car.__auth_key:
            self.validity = "Valid :)"
        else:
            self.validity = "Invalid :("


# Ask the user for car details
Name = input("Enter the Car Name: ")
Model = input("Enter the Car Model: ")
Key = int(input("Enter the key: "))

# Create an instance of the Car class
car = Car(Name, Model, Key)

# Print car details
print(f"Name: {car.name}\nModel: {car.model}\nKey: {car.key}\nValidity: {car.validity}")
