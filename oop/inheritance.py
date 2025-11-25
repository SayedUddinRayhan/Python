
# Single Inheritance

class GrandFather:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Father(GrandFather):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

grandFather1 = GrandFather("Jamal Uddin","White")
father1 = Father("Sobuj","Black", 56)
print(f"Father Name: {father1.name}, Color: {father1.color}, Age: {father1.age}")