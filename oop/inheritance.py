
# Single Inheritance

class GrandFather:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Father(GrandFather):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

# grandFather1 = GrandFather("Jamal Uddin","White")
# father1 = Father("Sobuj","Black", 56)
# print(f"Father Name: {father1.name}, Color: {father1.color}, Age: {father1.age}")

# Multiple Inheritance

class Uncle:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

class Cousin(Father, Uncle):
    def __init__(self, name, color, age, profession):
        Father.__init__(self, name, color, age)
        Uncle.__init__(self, name, profession)

Cousin1 = Cousin("Rafiq","Brown", 30, "Engineer")
print(f"Cousin Name: {Cousin1.name}, Color: {Cousin1.color}, Age: {Cousin1.age}, Profession: {Cousin1.profession}")





# Multi-Level Inheritance
class Son(Father, GrandFather):
    def __init__(self, name, color, age, school):
        super().__init__(name, color, age)
        self.school = school

# son1 = Son("Rayhan","Brown", 20, "Feni University")
# print(f"Son Name: {son1.name}, Color: {son1.color}, Age: {son1.age}, School: {son1.school}")