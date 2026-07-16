# Task 1: Create a Dictionary of Student Marks
# ----------------------------------------------
# This program stores student names and marks in a dictionary,
# asks the user for a student's name, and displays their marks.
# If the name is not found, it shows an appropriate message.

# Step 1: Create a dictionary of student marks
student_marks = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 76,
    "Sneha": 88,
    "Karan": 65
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ").strip()

# Step 3 & 4: Retrieve marks if found, else display a message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Sorry, '{name}' not found in the records.")
