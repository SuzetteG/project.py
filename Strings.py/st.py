message = "Hello, World!"
print(message.upper())  # Output: HELLO, WORLD!
print(message.lower())  # Output: hello, world!
text = " Python "
print(text.strip())  # Output: Python

message = "Hello, World!"
print(message.replace("World", "Python"))  # Output: ['Hello', ' Python!']

sentence = "Python is fun"
words = sentence.split()  # Output: ['Python', 'is', 'fun']

filename= "report.pdf"
print(filename.endswith(".pdf"))  # Output: True

my_string= 'Coding Temple is the best bootcamp ever!'
#Outputs should be:
#1. 'Coding Temple is the best bootcamp ever!'
#2. 'Coding Temple is the best bootcamp ever!'
#3. 'Coding temple is the greatest bootcamp ever!'
#4. ['Coding', 'Temple', 'is', 'the', 'best', 'bootcamp', 'ever!']

name= "Jenny"
age= "31"
print("My name is {} and I am {} years old.".format(name,age)) 
#Output: My name is Jenny and I am 31 years old.

name= "Alice"
age= 29
print(f"My name is {name} and I am {age} years old.")
#Output: My name is Alice and I am 29 years old.

first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]
import random
f_name = random.choice(first_names)
l_name = random.choice(last_names)
print(f"{f_name} {l_name}")
#Output: Randomly selected full name from the lists, e.g., "Dylan Peck"