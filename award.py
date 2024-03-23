
""" 

start


Collect times taken to complete individual triathlon events - swimming, cycling, running.

Calculate and display total time taken to complete the triathlon.

Display award to be received based on the following times:
    if total time is between 0 and 100 mins ==> Provincial Colours
    if total time is between 101 and 105 mins ==> Provincial Half Colours
    if total time is between 106 and 110 mins ==> Provincial Scroll
    if total time is >= 111 ==> No award


stop


"""

# Ask user to enter event times in minutes
print("Please enter your event time in minutes below!")
# Enter time taken to complete an event
swimming = input("Enter swimming time: ")
cycling = input("Enter cycling time: ")
running = input("Enter running time: ")

# Convert values entered to integers
swimming = int(swimming)
cycling = int(cycling)
running = int(running)

# Calculate and display total time taken to complete triathlon
total_time = swimming + cycling + running
print("Total time taken to complete triathlon: " + str(total_time) + " mins.")

# Display award to be received if total time is between 0 and 100 minutes
if total_time in range(101):
    print("Award to be received - Provincial Colours")
# Display award to be received if total time is between 101 and 106 minutes
elif total_time in range(101, 106):
    print("Award to be received - Provincial Half Colours")
# Display award to be received if total time is between 106 and 111 minutes
elif total_time in range(106, 111):
    print("Award to be received - Provincial Scroll")
# Display award to be received if total time is 111 minutes and above
elif total_time >= 111:
    print("No award")
