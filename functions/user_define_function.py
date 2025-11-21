
# Input + return
def add_two_numbers(a, b): # Function definition with arguments a and b
    return a + b

result = add_two_numbers(5, 7) # Function call with parameters 5 and 7
print("The sum is:", result)


# No input + return
def get_greeting(): # Function definition with no arguments
    return "Hello, welcome to Python functions!"

greeting = get_greeting() # Function call
print(greeting)

# Input + no return
def print_square(num): # Function definition with argument num
    print("The square of", num, "is", num ** 2)

print_square(4) # Function call with parameter 4

# No input + no return
def display_message(): # Function definition with no arguments
    print("This is a simple message from a function.")

display_message() # Function call