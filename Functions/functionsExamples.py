# Functions

# name_printer() - write a function that takes a name as an argument and prints it

# for i in collection
# i = 10

# defining a function
# name_printer("Jim")

def name_printer(name): # function header
    print(name)

# called my function
name_printer("Joe")
name_printer("Dylan")

# num_adder() - write a function that adds 1 + 1 and returns the value

def num_adder(): # its okay to have no arguments
    n = 1 + 1
    return n
    print(n)

result = num_adder()
print(result)
# print(n)

# name_splitter() - write a function that takes a full name as one string,
# and prints "last name, first name"

# "Samuel Bernsen" - full_name
# Bernsen, Samuel

def name_splitter(full_name):
    full_name = full_name.split() # redefines as a list of hopefully 2 elements
    first_name = full_name[0] # first_name is now the first string in the list
    last_name = full_name[1] # last_name is now the second string in the list
    print(last_name + ", " + first_name) # prints in desired format


name_splitter("John Doe")
name_splitter("Jane Doe")
print()

# squared() - write a function that returns the square of a given number

def squared(num):
    return num ** 2

print(squared(4)) # if not interested in saving value returned
# it's okay to just print

# for when you want to save your value
result = squared(4) # can be used later in the program
print(result)


# namespaces
# add_one - write a function that takes in a number, num, adds 1 to it, and prints it

# define
def add_one(num):
    num += 1
    print(num)

num = 5
print(num) # 5
num = add_one(num) # 6
print(num) # 6

# greater_than_10() - write a function that returns True if a given number is > 10, False otherwise

def greater_than_10(num):
    if num > 10:
        return True
    else:
        return False

# Try on your own

# 1. Write a function, sphere_volume() that takes the radius of a sphere and returns the volume. 
# Use the value of pi from the math library.
# Volume of a sphere = 4/3 * pi * r^3

# import statements go first
import math

def sphere_volume(r):
    return round(4/3 * math.pi * r**3, 3)

print(sphere_volume(3))

# 2. Use your former class work to create a function 
# that takes in the side lengths of a triangle
# and outputs the type of triangle given.
# (equilateral, ososceles, or scalene)

# Function implementation
def triangleType(side1, side2, side3):
    # side1 = input("Length 1: ")
    # side2 = input("Length 2: ")
    # side3 = input("Length 3: ")
    if (side1) == (side2) == (side3):
        print("equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isosceles")
    else:
        print("scalene")

# Function invocation
triangleType(5,5,5)
triangleType(5,6,6)
triangleType(5,6,7)

# multiple arguments
# write a function called calc_product() that takes two numbers and returns the product

def calc_product(num1, num2):
    return num1 * num2

print(calc_product(2, 3))
# print(calc_product())
calc_product(num2 = 3, num1 = 2)

# default arguments
# Write a function called menu_printer() that has a pre-set 3 course menu,
# but allows the user to pass in other choices if desired. 
# Print the menu to the user.

"Steve Jobs".split() # example with a default argument of " "


def menu_printer(app, entree = "Chicken", dessert = "Pie"):
    print("You are having", app, "to start")
    print("You are having", entree, "for a main")
    print("You are having", dessert, "for dessert")

app = input("Please enter your appetizer")
menu_printer(app = app)
# menu_printer("Soup", "Steak", "Ice Cream")
# menu_printer(entree = "Lobster")
# menu_printer("Soup", "Steak")
# menu_printer(dessert = "Cake")


# How can I return more than one value from a function?

# Write a function that takes in 2 numbers
# add 5 to the first number
# add 3 to second number
# return both

# returning a compound object ALWAYS returns a tuple
def num_adder(num1, num2):
    num1 = num1 + 5
    num2 = num2 + 3
    return num1, num2 # returning a compound object

result = num_adder(3, 4)
print(type(result))

num1, num2 = num_adder(3, 4)
print(num1, num2)
print(type(num1))



