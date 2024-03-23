'''
Start

Continually ask user to enter a number
Stop the program only if the user enter -1
Calculate and print out the average of all the numbers entered, excluding -1

Stop
'''


total = 0  # total is the variable where the sum of all the numbers entered will be stored
count = 0  # count is the variable that stores the number of entries from a user
user_number = 0

while user_number != -1:
    # ask user to enter number
    user_number = int(input("Enter a number: "))

    if user_number != -1:
        # add all user numbers entered and store in 'total' variable
        total += user_number
        count += 1

# Chech that count is greater than 0 to avoid zerodivision error
if count > 0:
    average = total / count
    print("The average of numbers entered is: ", average)
else:
    print("No valid numbers entered.")
    
    

