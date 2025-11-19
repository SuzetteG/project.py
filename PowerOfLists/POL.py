#Key Characteristics of Lists in Python:
# Ordered: Elements have a defined order, and that order will not change unless you explicitly reorder the list.
# Mutable: You can change, add, and remove elements after the list has been created.
# Allows Duplicate Elements: Lists can have items with the same value.
# Defined using square brackets [] and elements are separated by commas.
# Creating a list

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.14, True]

#Order:Items have a specific order
#Indexing: Items in a list are indexed starting from 0
#Elments are accessed by their index 

my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple

#Use negative indexing to access elements from the end of the list
print(my_list[-1])  # Output: cherry

#Add an item: .append() adds an item to the end of the list
my_list.append("orange")

#Insert at a specific index: .insert(index, item) adds an item at the specified index
my_list.insert(1, "blueberry")  # Inserts 'blueberry' at index 1

#Remove an item by value: .remove(item) removes the first occurrence of the item
my_list.remove("apple")

#Delete by index: Use del keyword or .pop() to remove an item at a specific index
del my_list[0] # Deletes the item at index 0
my_list.pop(1) # Removes and returns the item at index 1

#Slicing allows you to access a subset of items in a list 
my_list = [1, 2, 3, 4, 5, 6]
subset = my_list[1:4] # Output: [2, 3, 4]

#Omit the start or end index to slice from the beginning or to the end
print(my_list[:3])  # Output: [1, 2, 3]
print(my_list[3:])  # Output: [4, 5, 6]

my_list = ["apple", "banana", "cherry", "date"]
print(my_list[0])  # Output: apple
print(my_list[-1])  # Output: date
my_list.append("elderberry")
print(my_list)
my_list.insert(2, "blueberry")
print(my_list)
my_list.remove("banana")
print(my_list)
my_list.pop(1)
print(my_list)
my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]
print(subset)  # Output: [2, 3, 4]
print(my_list[:3])  # Output: [1, 2, 3]
print(my_list[3:])  # Output: [4, 5]

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])      # Print the first item
print(fruits[-1])     # Print the last item using negative indexing
fruits.append("elderberry")      # Add 'elderberry' to the end
fruits.insert(1, "blueberry")   # Add 'blueberry' at index 1
print(fruits)                    # Show updated list
fruits.remove("banana")        # Remove 'banana' from the list
del fruits[0]                  # Delete the first item from the list
print(fruits)                  # Show updated list
citrus_fruits = fruits[1:3]   # Slice from index 1 to 3 (exclusive)
print(citrus_fruits)          # Print the subset

#Built in Functions:
# len(): Returns the number of items in a list
len([1, 2, 3, 4,])  # Output: 4
# min(): Returns the smallest item in a list
min([5, 3, 8])  # Output: 3
# max(): Returns the largest item in a list
max([5, 3, 8])  # Output: 8
#.sort(): Sorts the list in ascending order
numbers = [4, 1, 7, 3]
numbers.sort() # Output: [1, 3, 4, 7]
#.reverse(): Reverses the order of the list
numbers.reverse() # Output: [7, 4, 3, 1]
#.extend(): Adds elements from another list to the end of the current list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) # Output: [1, 2, 3, 4, 5, 6]
#You can also generate lists together. list1 + list2
combined_list = list1 + list2  # Output: [1, 2, 3, 4, 5, 6]

#Nested Lists: Lists can contain other lists as elements
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])  # Output: 2 (accessing the second element of the first list)

# Final Challenge: Favorite Books
favorite_books = []
first_book = input("Enter your favorite book #1: ")
second_book = input("Enter your favorite book #2: ")
third_book = input("Enter your favorite book #3: ")
favorite_books.append(first_book)
favorite_books.append(second_book)
favorite_books.append(third_book)   

favorite_books.sort()
print("Your favorite books in sorted order:", favorite_books)
