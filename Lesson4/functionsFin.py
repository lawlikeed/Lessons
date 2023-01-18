# Objective: Create functions and make function calls





# Function for addition
def add(x,y):
    return x+y

# Function for subtraction
def subtract(x,y):
    return x-y

# Function for multiplication
def multiply(x,y):
    return x*y

# Function for division
def divide(x,y):
    return x/y



print(add(2,5))
print(subtract(2,5))
print(multiply(2,5))
print(divide(2,5))


x, y = input('Enter two numbers for addition: ').split()
# If you want more info on the split method visit https://www.w3schools.com/python/ref_string_split.asp

# print(f'x: {x}, type: {type(x)}')
# print(f'y: {y}, type: {type(y)}')

# Use user input for add function call
print(add(int(x), int(y)), '\n')

# Use user input for subtract function call
x, y = input('Enter two numbers for subtraction: ').split()
print(subtract(int(x), int(y)), '\n')

# Use user input for multiply function call
x, y = input('Enter two numbers for multiplication: ').split()
print(multiply(int(x), int(y)), '\n')

# Use user input for divide function call
x, y = input('Enter two numbers for division: ').split()
print(divide(int(x), int(y)), '\n')