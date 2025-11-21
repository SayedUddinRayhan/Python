
def my_function(**kwargs):
    print("Keyword arguments received:", kwargs)
    print("Type of kwargs:", type(kwargs))

    print(f"My name is {kwargs['name']}. I am {kwargs['age']} years old and I live in {kwargs['city']}.")

my_function(name="Sayed", age=26, city="Feni")