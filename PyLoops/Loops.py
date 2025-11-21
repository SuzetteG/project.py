#Loops allow a block of code to be executed repeatedly until a condition is met. 
# They are used for tasks such as iterating over a sequence of data, processing each item 
# in a list, or repeatedly checking a condition.
# There are two main types of loops in Python: for loops and while loops.
# For Loop:  Iterates over a sequence (e.g., list, tuple, string, or range) 
# and executes a block of code for each item in the sequence.
# While Loop: Repeats a block of code as long as a specified condition is true.
#For Loop Example
#Syntax:
#for item in iterable:
    # Code block to be executed
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# --> apple
# --> banana
# --> cherry
for i in range(5): #for loop
    print(i)    
# --> 0
# --> 1
# --> 2
# --> 3
# --> 4
#While Loop Example
#Syntax:
#while condition:
    # Code block to be executed
#Basic While Loop:
count = 0
while count < 5:
    print(count)
    count += 1
# --> 0
# --> 1
# --> 2
# --> 3
# --> 4

count = 0
while count <= 20:
    print(count)
    count += 2   
# --> 2  
# -- > 4  
# --> 6  
# --> 8
# -- > 10  
# --> 12
# --> 14
# -- > 16 
# --> 18
# --> 20

#Control Flow in Loops
#Break Statement: Exits the loop prematurely when a certain condition is met.
for i in range(10):
    if i == 5:
        break
    print(i)
# --> 0
# --> 1
# --> 2
# --> 3
# --> 4
#Continue Statement: Skips the current iteration and moves to the next one.
for i in range(5):
    if i == 3:
        continue
    print(i)
# --> 0
# --> 1
# --> 2
# --> 4

count = 1
while count < 31:
    print(count)
    count += 1
# --> 1
# --> 2
# --> 3
# --> 4
# --> 5
# --> 6
# --> 7
# --> 8
# --> 9
# --> 10
# --> 11
# --> 12
# --> 13
# --> 14
# --> 15
# --> 16
# --> 17
# --> 18
# --> 19
# --> 20
# --> 21
# --> 22
# --> 23
# --> 24
# --> 25
# --> 26
# --> 27
# --> 28
# --> 29
# --> 30

for num in range(1, 30):
    if num % 3 == 0:
        continue
    print(num)
# --> 1
# --> 2
# --> 4
# --> 5
# --> 7
# --> 8
# --> 10
# --> 11
# --> 13
# --> 14
# --> 16
# --> 17
# --> 19
# --> 20
# --> 22
# --> 23
# --> 25
# --> 26
# --> 28
# --> 29

for num in range(1, 31):
    if num > 25:
        break
    print(num)
# --> 1
# --> 2
# --> 3
# --> 4
# --> 5
# --> 6
# --> 7
# --> 8
# --> 9
# --> 10
# --> 11
# --> 12
# --> 13
# --> 14
# --> 15
# --> 16
# --> 17
# --> 18
# --> 19
# --> 20
# --> 21
# --> 22
# --> 23
# --> 24
# --> 25