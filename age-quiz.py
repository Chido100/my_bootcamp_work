
# Ask user for thier age - Only accept integer 
age = int(input("Enter age: "))

# Check user age is below 13
if age < 13:
    print("You qualify for the kiddie discount.")
# Check user age is 21
elif age == 21:
    print("Congrats on your 21!")
# Check user age is above 100
elif age > 100:
    print("Sorry, you're dead.")
# Check user age is 65 or above
elif age >= 65:
    print("Enjoy your retiremnet!")
# Check user age is 40 or above
elif age >= 40:
    print("You're over the hill")
# Check for any other age
else:
    print("Age is but a number.")

