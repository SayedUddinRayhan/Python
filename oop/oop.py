# Constructors
# Constructors are special methods that are automatically called when an object of a class is created.
# They are typically used to initialize the attributes of the object. with no return pe
# There are three types of constructors in Python:
# 1. Default Constructor: A constructor that takes no parameters and initializes the object with default values
# 2. Parameterized Constructor: A constructor that takes parameters to initialize the object with specific values 
# 3. Default value Constructor: A constructor that takes parameters with default values

# class er vetor function ke method bola hoy
# class er baire function ke function bola hoy
class Car:
    # Default Constructor
    def __init__(self):   # dunder method. Self ei car class er object ke indicate kore
        self.brand = ""
        self.model = ""

    # Parameterized Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Default value Constructor
    def __init__(self, brand="Unknown", model="Unknown"):
        self.brand = brand
        self.model = model

# my_car = Car()
# my_car.brand = "Toyota"
# my_car.model = "Corolla"

# print("Car Brand:", my_car.brand)
# print("Car Model:", my_car.model)

# my_car2 = Car()
# my_car2.brand = "Honda"
# my_car2.model = "Civic"

# print("Car Brand:", my_car2.brand)
# print("Car Model:", my_car2.model)

# car_obj = Car("Ford", "Mustang")
car_obj = Car()
print("Car Brand:", car_obj.brand)
print("Car Model:", car_obj.model)