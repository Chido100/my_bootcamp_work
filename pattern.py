
# Iterate over the number of rows => 5
for i in range(1, 2 * 5):   # multiplyimg 2 by the number of rows (5) is to indicate the first and second halves of the pattern
    
    # display first half of the pattern
    if i <= 5:
        stars = "*" * i
    # display second half of the pattern
    else:
        stars = "*" * (2 * 5 - i)
    
    print(stars)


