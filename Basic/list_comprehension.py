a = [1, 2, 3, 4, 5]

# for i in range(len(a)): 
#     if a[i] % 2 == 0:
#         a[i] = a[i]**2

# print(a)

# i = 0

# while i < len(a):
#     if a[i] % 2 == 0:
#         a[i] = a[i]**2
#     i += 1
# print(a)

# List Comprehension
print([i**2 if i % 2==0 else i for i in a])