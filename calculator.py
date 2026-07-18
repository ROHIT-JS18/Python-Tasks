"""
Tkinter Calculator Application
-------------------------------
A GUI calculator built with Python's Tkinter library.

This version does NOT use eval(). All arithmetic is performed with
custom functions (add, subtract, multiply, divide), and the
calculator keeps track of the first number, the chosen operator,
and the second number itself, then calls the matching function
to compute the result.
"""

import tkinter as tk


# ---------- Custom arithmetic functions (no eval!) ----------

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def calculate(first_num, second_num, operator):
    """
    Dispatch to the correct arithmetic function based on the
    operator string ('+', '-', '*', '/').
    """
    if operator == "+":
        return add(first_num, second_num)
    elif operator == "-":
        return subtract(first_num, second_num)
    elif operator == "*":
        return multiply(first_num, second_num)
    elif operator == "/":
        return divide(first_num, second_num)
    else:
        raise ValueError(f"Unknown operator: {operator}")


def format_result(value):
    """
    Display integers without a trailing '.0' (e.g. 8 instead of 8.0),
    but keep decimals for non-whole results.
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


# ---------- Calculator state ----------
# These track the two operands and the chosen operator so the
# calculator can compute the result without eval().

first_number = None      # First operand (float) once an operator is pressed
pending_operator = None  # The operator chosen ('+', '-', '*', '/')
start_new_number = False # True when the next digit should start a fresh number


# ---------- Functions to handle button actions ----------

def button_click(digit):
    """Append the clicked digit to the display field."""
    global start_new_number

    current = entry_field.get()

    # If we just pressed an operator or equals, start a fresh number
    if start_new_number or current == "0":
        entry_field.delete(0, tk.END)
        start_new_number = False

    entry_field.insert(tk.END, digit)


def button_decimal():
    """Add a decimal point, avoiding duplicates in the current number."""
    global start_new_number

    if start_new_number:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "0")
        start_new_number = False

    current = entry_field.get()
    if "." not in current:
        entry_field.insert(tk.END, ".")


def button_operator(operator):
    """
    Store the number currently on screen as the first operand and
    remember which operator was chosen. The display is left as-is
    so the user can see their first number; the next digit press
    will start entering the second number.
    """
    global first_number, pending_operator, start_new_number

    try:
        first_number = float(entry_field.get())
    except ValueError:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")
        return

    pending_operator = operator
    start_new_number = True


def button_equal():
    """
    Read the second number from the display, run the matching
    custom arithmetic function via calculate(), and show the result.
    """
    global first_number, pending_operator, start_new_number

    if first_number is None or pending_operator is None:
        return  # Nothing to calculate yet

    try:
        second_number = float(entry_field.get())
        result = calculate(first_number, second_number, pending_operator)

        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, format_result(result))

    except ZeroDivisionError:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error: Div by 0")

    except ValueError:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

    finally:
        first_number = None
        pending_operator = None
        start_new_number = True


def button_clear():
    """Clear the display field and reset calculator state."""
    global first_number, pending_operator, start_new_number

    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, "0")
    first_number = None
    pending_operator = None
    start_new_number = False


# ---------- Main window setup ----------

window = tk.Tk()
window.title("Tkinter Calculator")
window.resizable(False, False)

# ---------- Entry field (display) ----------

entry_field = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=5,
                        justify="right")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry_field.insert(tk.END, "0")

# ---------- Button layout ----------
# Each tuple: (label, row, column)
digit_buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0), (".", 4, 1),
]

operator_buttons = [
    ("/", 1, 3), ("*", 2, 3), ("-", 3, 3), ("+", 4, 3),
]

# Digit buttons (and decimal point)
for (text, row, col) in digit_buttons:
    if text == ".":
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                         command=button_decimal)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                         command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Operator buttons
for (text, row, col) in operator_buttons:
    btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                     bg="#2196F3", fg="white",
                     command=lambda t=text: button_operator(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(window, text="C", width=5, height=2, font=("Arial", 14),
                       bg="#f44336", fg="white", command=button_clear)
clear_btn.grid(row=4, column=2, padx=5, pady=5)

# Equals button
equal_btn = tk.Button(window, text="=", width=11, height=2, font=("Arial", 14),
                       bg="#4CAF50", fg="white", command=button_equal)
equal_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

# ---------- Start the application ----------

if __name__ == "__main__":
    window.mainloop()
