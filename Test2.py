## this is the Class and Methods section, class is the first, the the actions is the mothods after the first def ##

class Dog:
    # Constructor to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")
    
    # Another instance method that modifies an attribute
    def set_age(self, new_age):
        self.age = new_age
    
    # Instance method that returns a value
    def get_age(self):
        return self.age

# Creating an instance of the class
my_dog = Dog("Buddy", 5)

# Calling instance methods
my_dog.bark()           # Output: Buddy says Woof!
my_dog.set_age(6)       # Modifies the dog's age
print(my_dog.get_age()) # Output: 6



# Parent class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def start(self):
        print(f"The {self.brand} vehicle is starting.")

# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def start(self):  # Overriding the start method
        print(f"The {self.model} car is starting.")

# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, year, type_bike):
        super().__init__(brand, year)
        self.type_bike = type_bike

    def start(self):  # Overriding the start method
        print(f"The {self.type_bike} bike is starting.")

# Create objects
my_car = Car("Toyota", 2020, "Corolla")
my_bike = Bike("Yamaha", 2019, "Sports")

# Call methods
my_car.start()  # Output: The Corolla car is starting.
my_bike.start() # Output: The Sports bike is starting.