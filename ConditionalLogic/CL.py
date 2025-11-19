#Key Concepts: 
# if: Used to test if a condition is true
# elif: Used to test multiple conditions
# else: Used to execute code when none of the conditions are true

raining = True  # Change to False to test the other branch
if ( raining ):
    print("Take an umbrella.")
else:
    print("Wear Sunglasses.")

# Syntax
#if ( condition ): 
#   --- code to execute if condition is true ---
#elif another_condition:
#   --- code to execute if another_condition is true ---
#else:
#   --- code to execute if none of the above conditions are true ---

x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else: 
    print("x is negative")

#Comparison Operators:
# == : equal to
# != : not equal to
# >  : greater than
# <  : less than
# >= : greater than or equal to
# <= : less than or equal to    

#Logical Operatores:
# and : returns True if both conditions are true
# or  : returns True if at least one condition is true
# not : negates the condition

age = 25
is_student = True

if age < 18 and is_student:
    print("Eligible for student discount.")
else:
    print("Not eligible for student discount.")

# Pitfall: all conditions are checked 
if x > 0: 
	print("Positive") 
if x == 0: 
	print("Zero") 
else: 
	print("Negative") 

# Correct approach using elif 
if x > 0: 
	print("Positive") 
elif x == 0: 
	print("Zero") 
else: 
	print("Negative")
bootcamp = 'coding temple'

# Incorrect Way:
# if (bootcamp = 'coding temple'): # would throw an error
#     print('best bootcamp ever!')

# Correct Way:
if (bootcamp == 'coding temple'):
	print('best bootcamp ever!')

#Final Challenge
#Randomly select a number between 1 and 10
#Ask the user to guess the number
#If the user is correct, print "Congratulations! You guessed the number."
#If the user is too low, print "Too low! Try again."
#If the user is too high, print "Too high! Try again."

import random

secret_num = random.randint(1, 10)
guess = (int(input("Guess the number (between 1 and 10): ")))

if guess == secret_num:
    print("Congratulations! You guessed the secret number.")
elif guess < secret_num:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")
