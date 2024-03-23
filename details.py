'''

Start


Ask user for the following details - ["name", "age", "house number", "street name"]

Concatinate the entered details in a single sentence

Print out the sentence


Stop


'''

# Ask user for details
name = input("What is your name? ")
age = int(input("How old are you? "))
house_number = input("What is your house number? ")
street_name = input("What is your street name? ")

user_details = f"This is {name.title()}. Hes is {age} years old and lives at house number {house_number}, on {street_name.title()}."
print(user_details)