
n = 10 # Flobal variable
def func():
    print("Inside func:", n)  # Accessing global variable n

func()

print("Outside func:", n)  # Accessing global variable n

def func_with_local():
    x = 5  # Local variable
    print("Inside func_with_local:", x)  # Accessing local variable x

func_with_local()

# print("Outside func_with_local:", x)  # Accessing local variable x
                                     # This will raise a NameError

# LEGB Rule Example
x = 'global x'  # Global scope
def outer_function():
    x = 'enclosing x'  # Enclosing scope

    def inner_function():
        x = 'local x'  # Local scope
        print("Inside inner_function:", x)  # Accessing local variable x

    inner_function()
    print("Inside outer_function:", x)  # Accessing enclosing variable x

outer_function()

print("In global scope:", x)  # Accessing global variable x

# Using global keyword
y = 5  # Global variable   
def modify_global():
    y = 10 # Enclosing variable
    def inner_modify():
        global y  # Declare y as global
        # nonlocal_y = y  # Accessing global variable y
        y = 20    # Modify global variable y
        print("Inside inner_modify:", y)  # Accessing modified global variable y
    print("Before inner_modify:", y)  # Enclosing variable change hoy na
modify_global()
print("Outside modify_global:", y)  # Accessing modified global variable y

# global -> global variable k change korte pare
# nonlocal -> enclosing variable k change korte pare