"""Alternate characters"""

# Input string to alternate characters
user_input = input("Enter a string: ")

# Split the string into a list of characters
input_list = list(user_input)

# Convert alternate characters to uppercase and lowercase, respectively
for i in range(len(input_list)):
    if i % 2 == 0:
        input_list[i] = input_list[i].lower()
    else:
        input_list[i] = input_list[i].upper()

# Join the list of characters back into a string
result_str = ''.join(input_list)

# Display the result
print("Result:", result_str)



"""Alternate words"""

# Input string to alternate words
user_input2 = input("Enter a string: ")

# Split the string into a list of words
word_list = user_input2.split()

# Convert alternate words to uppercase and lowercase, respectively
for i in range(len(word_list)):
    if i % 2 == 0:
        word_list[i] = word_list[i].lower()
    else:
        word_list[i] = word_list[i].upper()

# Join the list of words back into a string
result_str = ' '.join(word_list)

# Display the result
print("Result:", result_str)



