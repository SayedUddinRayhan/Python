
# lambda parameters: expression
add = lambda x, y: x + y

square = lambda x: x**2

print("The sum is:", add(3, 5))
print("The square is:", square(4))

print("The sum is:", (lambda x, y: x + y)(10, 15))

n = [1, 2, 3 , 4]

squared = lambda x: [i**2 for i in x]
print("Squared list:", squared(n))

squared_map = list(map(lambda x: x**2, n))
print("Squared list using map:", squared_map)

items = [(1, 5), (2, 1), (3, 3)]

sorted_items = sorted(items, key=lambda x: x[1])
print("Sorted items by second element:", sorted_items)

students = [('Sayed', 95), ('Rayhan', 85), ('Arafat', 90)]

sorted_students = sorted(students, key=lambda x: x[1])
print("Students sorted by score:", sorted_students)

x = [1,2,3,4]
# map(ki korte chacchi, kar upor apply korte chacchi)
squared_x = list(map(lambda i: i**2, x))
print("Squared using map:", squared_x)


# filter(ki korte chacchi, kar upor apply korte chacchi)
even_numbers = list(filter(lambda i: i % 2 == 0, x))
print("Even numbers using filter:", even_numbers)

# reduce(ki korte chacchi, kar upor apply korte chacchi)
from functools import reduce
product = reduce(lambda a, b: a * b, x)
print("Product using reduce:", product)   

result = reduce(lambda a, b: a if a > b else b, [10, 5, 8, 20])
print(result)   # 20

digits = [1, 2, 3, 4]

# Convert digits into a number
num = reduce(lambda x, y: x * 10 + y, digits)
print(num)  # 1234