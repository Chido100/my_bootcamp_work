# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"    # Added quotations to the value of the variable
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Added "f" to the string, moved the placements of "{number_of_teeth}" and {animal_type} to each others positions

print(full_spec)  # Removed space in print statement, added parenthesis to the print statement