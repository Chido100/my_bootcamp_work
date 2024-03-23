# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Added paranthesis to the print statement
print("\n") # Removed indetation and added parenthesis to teh print statement

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old" # Removed indentation, replaced the double "=="sign to "=" and corrected variable name

age = int(age_str[:2])  # Fixed indetation, corrected variable name "age_Str" and also added string slicing to make sure the age variable only selects the number value

print("I'm " + str(age) + " years old.") # Fixed indetation, added casting (str) to the age to ensure concatination and added spaces at the end and beginning of each strings respectively

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5  # Change value of varibale to 3.5 to indicate 3years and 6months and from str to int by removing quotes in value

total_years = age + years_from_now

print("The total number of years: " + str(total_years)) # Replaced "answer_years" string with casted "total_years" variable to str for concatination

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Replaced "total" with "total_years"

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer