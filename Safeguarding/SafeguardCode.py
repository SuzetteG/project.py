# What are Errors and Exceptions in Python?
# Errors are issues in the code that prevent it from running. 
# Syntax errors occur when the Python interpreter encounters a statement that breaks the 
# rules of the language.
# Exceptions are events that occur during execution that disrupt the normal flow of a program.
# Common exception types include ValueError, TypeError, IndexError, KeyError, and ZeroDivisionError.

# Syntax Error
if True:
    print("Hello")  # Corrected: added colon

# Runtime Exception
# x = 1 / 0  # This will raise ZeroDivisionError (commented out for testing)

# Basic exception handling with try and except
# The try block lets you test a block of code for errors, 
# while the except block lets you handle the error.
try:
    # Code that may raise an exception
    x = int('not_a_number')
except Exception:
    # Code that runs if an exception occurs
    print("An exception occurred!")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#Write a program that prompts the user for 2 numbers and divides the first number by the second.
# It should handle the exceptions where the user enters invalid data (non-numeric input) or 
# attempts to divide by zero.
try:
    # Step 1: Prompt user to input two numbers
    num1 = 10  # Hardcoded value for testing
    num2 = 2   # Hardcoded value for testing
    # Step 2: Convert inputs to integers or floats
    num1 = float(num1)
    num2 = float(num2)
    # Step 2c: Perform the division
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ValueError:
    # Step 2a/2b: Prompt user to input two numbers & convert inputs to integers or floats.
    # Step 2c: Perform the division
    # Step 3a: Handle non-numeric input
    pass
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    # Step 3b: Handle division by zero

# Catching Multiple Exceptions: You can handle multiple exceptions by specifying them as a 
# tuple in a single except block.
try:
    x = 5  # Hardcoded value for testing
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")

#Catching Multiple Exceptions in One Block: 
try:
    x = 0  # Hardcoded value for testing (will trigger ZeroDivisionError)
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

#Catching any Exceptions in one Block: 
try:
    x = 'abc'  # Hardcoded value for testing (will trigger ValueError)
    result = 10 / int(x)
except:
    print(f"An error occurred!")

# Else and finally clauses: 
# The else block runs if no exceptions were raised in the try block.
# The finally block runs no matter what, whether an exception was raised or not.
try:
    x = 2  # Hardcoded value for testing
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Execution complete!")

# Best practices for Exception Handling:
# 1. Be specific with exception types rather than a generic except.
# 2. Only use exceptions for error handling, not regular control flow.
# 3. Avoid swallowing exceptions silently without logging or taking action. 

#Final Challenge: Create a program that simulates an ATM withdrawal process.
# The program should: 
#1. Allow the user to input a withdrawal amount.
#2. Raise an exception if the input is invalid (non-numeric or negative).
#3. Ensure that the withdrawal amount doesn't exceed the account balance, raising an exception. 
#4. Always display the remaining balance, even if an error occurs. 
class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return self.balance
atm = ATM(2000)  # Initial balance of $2000
try:
    amount = 500  # Hardcoded value for testing
    remaining_balance = atm.withdraw(amount)
    print(f"Withdrawal successful! Remaining balance: ${remaining_balance:.2f}")
except InvalidAmountError as e:
    print(f"Error: {e}")
except InsufficientFundsError as e:
    print(f"Error: {e}")
finally:
    print(f"Remaining balance: ${atm.balance:.2f}")
