
def addition(*args):
    print("Arguments received:", args)
    print("Type of args:", type(args))
    return sum(args)

result = addition(1, 2, 3, 4, 5)
print("The sum is:", result)