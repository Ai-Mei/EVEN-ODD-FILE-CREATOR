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

def procedure():
# Open number.txt (read), even.txt (append) and odd.txt (append)
    with open("numbers.txt") as numbers_file, open("even.txt", "a") as even_integer, open("odd.txt", "a") as odd_integer:
# Check every line in the number.txt.
        for line in numbers_file:
            integer = int(line)
# If even, append the integer to even.txt.
            if integer % 2 == 0:
                even_integer.write(str(integer) + "\n")
# Else, if odd, append the integer to odd.txt.
            else:
                odd_integer.write(str(integer) + "\n")

# Run the procedure.
procedure()