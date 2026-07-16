# Task 2: Demonstrate List Slicing
# ----------------------------------------------
# This program creates a list of numbers from 1 to 10,
# extracts the first five elements, reverses them,
# and prints both the extracted and reversed lists.

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)

# Step 2: Extract the first five elements
first_five = numbers[:5]
print("First five elements:", first_five)

# Step 3: Reverse the extracted elements
reversed_five = first_five[::-1]

# Step 4: Print both lists
print("Extracted list:", first_five)
print("Reversed list:", reversed_five)
