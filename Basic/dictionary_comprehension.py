a = {1: 'Apple', 2: 'Banana', 3: 'Cherry', 4: 'Date'}

# for i in a:
#     print(i, a[i])

# output =
# 1 Apple
# 2 Banana
# 3 Cherry
# 4 Date

# for i in a.values():
#     print(i)

# output
# Apple
# Banana
# Cherry
# Date

# for i in a.items():
#     print(i)

# output
# (1, 'Apple')
# (2, 'Banana')
# (3, 'Cherry')
# (4, 'Date')

# Dictionary Comprehension
# print({i: a[i] for i in a})

# output
# {1: 'Apple', 2: 'Banana', 3: 'Cherry', 4: 'Date'}

# print({k: v for k, v in a.items()})

# output
# {1: 'Apple', 2: 'Banana', 3: 'Cherry', 4: 'Date'} 

# print({k: v.upper() for k, v in a.items() if k % 2 == 0})

# output
# {2: 'BANANA', 4: 'DATE'} 

print({k: v.upper() if k % 2 == 0 else v for k, v in a.items()})

# output
# {1: 'Apple', 2: 'BANANA', 3: 'Cherry', 4: 'DATE'} 