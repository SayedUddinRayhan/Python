
# Association Example
class Laptop():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Student():
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop  # Association: Student has a Laptop

laptop1 = Laptop("Dell", "XPS 13")
student1 = Student("Sayed", laptop1)

print(f"Student Name: {student1.name}, Laptop Brand: {student1.laptop.brand}, Laptop Model: {student1.laptop.model}")

# Aggregation Example
class Department():
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: Department has Employees

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee():
    def __init__(self, name):
        self.name = name

dept = Department("IT")
emp1 = Employee("Sayed")
dept.add_employee(emp1)
print(f"Department: {dept.name}, Employee: {dept.employees[0].name}")

# Composition Example
class Human():
    def __init__(self, name):
        self.name = name
        self.heart = Heart()  # Composition: Human has a Heart

class Heart():
    def __init__(self):
        self.beats_per_minute = 72
    
human1 = Human("Sayed")
print(f"Human Name: {human1.name}, Heart Beats per Minute: {human1.heart.beats_per_minute}")