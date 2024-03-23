'''

Start


Decalre a variable(String)
Print out the sentence after replacing all exclamation marks with spaces

Print out the sentence

Print out the sentence in all upper case

Print out the sentence in reverse 


Stop


'''

text = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Declare a new variable that replaces the exclamation marks with spaces 
new_text = text.replace("!", " ")
# Print sentence 
print(new_text)

# Print sentence in all upper case
print(new_text.upper())

# Reprint sentence in reverse
print(new_text[::-1])