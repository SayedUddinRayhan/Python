
class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name, position):
        self.name = name          # Instance variable
        self.position = position  # Instance variable

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def get_employee_details(self):
        return f"Name: {self.name}, Position: {self.position}, Company: {self.company_name}"
    
obj1 = Employee("Sayed", "Developer")

print("Company Name (using class method):", Employee.get_company_name()) # class method use korle class name diye call korte hoy
print("Employee Details (using instance method):", obj1.get_employee_details()) 
print("Employee Name (accessing instance variable):", obj1.name)