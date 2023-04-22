# # Open the numbers.txt.
with open("numbers.txt", "a") as numbers_file:
# numbers_file = open("numbers.txt", "a")



# Generate 20 random integers.
    import random
    i = 0
    for i in range (20):
        integer = random.randint(1, 100)
        numbers_file.write(str(integer) + "\n")
        print(integer)
        i += 1

numbers_file.close()