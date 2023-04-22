# Open the numbers.txt (Append)
with open("numbers.txt", "a") as numbers_file:

# Generate 20 random integers.
    import random
    i = 0
    for i in range (20):
        integer = random.randint(1, 100)
        numbers_file.write(str(integer) + "\n")
        print(integer)
        i += 1

# Open number.txt (read), even.txt (append) and odd.txt (append)
# Check every line in the number.txt.
# If even, append the integer to even.txt.
# Else, if odd, append the integer to odd.txt.

