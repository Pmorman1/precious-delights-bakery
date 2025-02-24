#Program Name: Assignment3.py
# Course: IT3883/Section XXX
# Student Name:Precious Morman
# Assignment Number: Assignment 3
# Due Date: 02/23/2025
# Purpose: This program converts Miles per Gallon into Kilometers per Liter. 
# The result is updated simultaneously as the user types, without the need for a button click.
# Specific resources used to complete the assignment: Help from a friend on understanding how to implement real-time conversion.

import tkinter as tk

# Conversion factor
MPG_TO_KM_L = 0.425143707

def convert_mpg_to_kml():
    """Converts Miles per Gallon to Kilometers per Liter."""
    try:
        # Get the value entered by the user and convert it to a float
        mpg = float(entry_mpg.get())
        
        # Perform the conversion
        kml = mpg * MPG_TO_KM_L
        
        # Update the result label with the converted value
        label_result.config(text=f"{kml:.4f} KM/L")
    except ValueError:
        # If the user enters invalid data (like a letter), show an error message
        label_result.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("MPG to KM/L Converter")

# Create the GUI elements (labels, entry boxes, etc.)
label_instructions = tk.Label(root, text="Enter Miles per Gallon (MPG):")
label_instructions.pack()

entry_mpg = tk.Entry(root)
entry_mpg.pack()

# Bind the entry box to update the result in real-time whenever the user types
entry_mpg.bind("<KeyRelease>", lambda event: convert_mpg_to_kml())

label_result = tk.Label(root, text="Enter a number to see the result.")
label_result.pack()

# Run the application
root.mainloop()

