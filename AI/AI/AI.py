#Using ChatGPT as a Personalized Python Mentor
# This script demonstrates how to use ChatGPT as a personalized Python mentor.
# AI can assist with code explanations, debugging, and learning new concepts.
# Example usage: 
# 1. Ask ChatGPT to explain a piece of code.
# 2. Request help with debugging errors.
# 3. Learn new Python concepts through interactive Q&A.
# "Explain Python string slicing like I'm a visual learner."
# Start a small coding task, and let AI guide you step-by-step.
# Task: Create a function that takes a list of numbers and returns only the odd numbers.

def get_odd_numbers(numbers):
    # Create an empty list to store odd numbers
    odd_numbers = []
    # Loop through each number in the input list
    for num in numbers:
        # Check if the number is not divisible by 2 (odd)
        if num % 2 != 0:
            # Add the odd number to the list
            odd_numbers.append(num)
    # Return the list of odd numbers
    return odd_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7]
print(get_odd_numbers(numbers))

# You can ask "How can I make this more efficient?" 
# "What would happen if I passed an empty list?"
# AI helps you debug faster and learn from mistakes. 
# Prompt to AI: "I got a TypeError.'int' object is not iterable." How do I fix it? What does it mean?
# AI can provide explanations and solutions to common errors.
# Asking how you can stay away from that error in the future turns into a learning opportunity.
#Prompt Ideas for Personalized Learning:
# “Build me a beginner Python project that teaches me about loops and conditionals.”
# “Give me 3 small practice problems for Python functions with step-by-step hints.”
# “Explain Python lists like I’m a visual learner.”
# “How can I practice Python if I only have 30 minutes a day?”
# Ask AI to "Create a beginner Python Challenge using strings and lists that takes 15 min to solve."

# Final Challenge: Learn with AI, Then Teach It Back
# Choose a topic you find tricky—like loops, lists, or functions.

#Ask ChatGPT to explain it to you.
#Build a tiny program that uses that concept.
#Ask AI to help you explain the code as if you were teaching it to someone else.
#This “teach-back” technique helps you retain what you’ve learned and communicate 
# it clearly—an essential workplace skill.
#Provide hints if necessary, and let AI guide you if you ask. 

# Asked chatgpt to explain Python Errors. 
# Explained syntax errors - it happens when 'grammar' of the code is wrong. 
# Ex. print("Hello 
# Missing closing quote causes syntax error.
# Common Syntax Errors: 
# Missing parentheses, Missing quotes, Missing colons (if, for, while, def, class), and
# Extra symbols (like two periods instead of one)")
# Runtime Errors - happen during execution. Code is syntactically correct but fails when run.
# Ex. dividing by zero, accessing undefined variables, file not found errors.
# x = 5 / 0  # This will raise a ZeroDivisionError at runtime.
# Common Runtime Errors: ZeroDivisionError, NameError, TypeError, FileNotFoundError
# Logical Errors - code runs without crashing but produces incorrect results.
# Ex. using + instead of * in a calculation.
# total = 10 + 5  # Intended to multiply, but added instead.
# Common Logical Errors: Incorrect calculations, Wrong variable usage, Faulty conditions in if statements or loops.
# Ask ChatGPT: "How can I avoid these errors in the future?"
#1. Always read the last line. 
#2. Check the line number. 
#3. Look at the code above that line too.
#4. Check for punctuation and typos. Python cares about 'grammar'. 
#5. Write in small chunks and check your opening code. 
#6. Always check your data types. 
#7. Validate input. Guard your code against unexpected values. 
