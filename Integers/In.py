a =10 #positive integer
b = -5 #negative integer
c = 0 #zero integer

x = 10
y = 5
print(x + y)  # Output: 15  # Addition
print(x - y)  # Output: 5  # Subtraction
print(x * y)  # Output: 50  # Multiplication
print(x / y)  # Output: 2.0  # Division (float result)
print(x % y)  # Output: 0  # Modulus
print(x // y)  # Output: 2  # Floor Division

milk = 5 
eggs = 3
coffee = 10
# Outputs should be: 
# --> "The total cost: $<total-of-items>"
# --> "Final amount after 10% discount: $<total-with-discount>"

print(2 ** 3) # Output: 8 # 2 raised to the power of 3
print(pow(2, 3)) # Output: 8 # Using pow function for exponentiation

print(abs(-10)) # Output: 10 # Absolute value
print(round(3.14)) # Output: 3 # Rounding to nearest integer
print(round(3.56)) # Output: 4 # Rounding to nearest integer

num_str = "123"
num = int(num_str)
print(num + 1)  # Output: 124

#Steps:
#1. Ask the user to input two numbers.
#2. Perform basic arithmetic operations (addition, subtraction, multiplication, division) on the inputs.
#3. Display the results. 

first_num = int(input("What is the first number?"))
second_num = int(input("What is the second number?"))

add = first_num + second_num
subtract = first_num - second_num
multiply = first_num * second_num
divide = first_num / second_num
divide_floor = first_num // second_num

print(add)
print(subtract)
print(multiply)
print(divide)
print(divide_floor)
