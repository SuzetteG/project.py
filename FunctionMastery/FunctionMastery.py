#Functions are reusable blocks of code that perform a specific task. 
# Instead of repeating code, we write a function once and call it whenever needed. 
# This makes code cleaner, more modular, and easier to maintain.
# Key Concepts: 
# What is a function? A block of organized, reusable code that performs a single action.
# Why use functions? To avoid code duplication, improve readability, and make debugging easier.
# Example: 
#def greet():
#    print("Hello, welcome to Coding Temple!")
# Defining and calling Functions
# Defining a function: use the def keyword followed by the function name and parentheses ().
# Calling a function: To utilize/run the function, use its name followed by parentheses ().
# Syntax: 
# def function_name():
    # code block

def greet():
    print("Hello, welcome!")
    
greet()  # --> Hello, welcome!
# Parameters and Arguments
# Parameters: Variables defined in the function declaration.
# Arguments: Values passed to the function when calling it.
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
    
greet("Alice")  # 'Alice' is an argument, output: Hello, Alice!

def introduce_yourself(name="Christian", hobby="gaming"):
    print(f"My name is {name} and I love {hobby}.")
introduce_yourself()  # Uses default values
introduce_yourself("Alice", "painting")  # Overrides default values
# Return Values
# Functions can return values using the return statement.
# This is useful when you want to get an output from a function and use it later.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

# Function Scope (Local vs Global Variables)
# Local Variables: Defined within a function and can only be accessed inside that function.
# Global Variables: Defined outside any function and can be accessed anywhere in the code.
x = 10  # global variable

def print_number():
    x = 5  # local variable
    print(x)  # Output: 5
    
print_number()
print(x)  # Output: 10

# Default parameters & variable-length arguments
# Default Parameters: Allow functions to have default values for parameters.
# Variable-Length Arguments: Allow functions to accept an arbitrary number of arguments 
# using *args and ** kwargs.
def add_numbers(*args):
    return sum(args)
    
print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(5, 10))    # Output: 15

list_of_numbers = [3, 99, 12, 1, 7]

def square_numbers(numbers):
    return [x ** 2 for x in numbers]

squared_list = square_numbers(list_of_numbers)
print(squared_list)  # Output: [9, 9801, 144, 1, 49]