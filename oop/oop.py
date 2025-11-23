
# default constructor
# parameterized constructor
# 



class Car:
    def __init__(self):   # dunder method. Self ei car class er object ke indicate kore
        self.brand = ""
        self.model = ""

my_car = Car()
my_car.brand = "Toyota"
my_car.model = "Corolla"

print("Car Brand:", my_car.brand)
print("Car Model:", my_car.model)