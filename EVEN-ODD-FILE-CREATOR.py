import pyfiglet
# Introduction.
print("===" * 50)
input("\033[0;32m\Welcome. \033[0;37mThis program will generate a unique set of \033[1;33m20 integers  \033[0;37mfor you.Then, the generated set of integers will be saved as text file named \033[1;33mnumbers.txt\033[0;37m\nThen, I will analyze the integers whether they are \033[1;31modd\033[0;37m or \033[1;34meven\033[0;37m and make another two files for \033[1;31modd integers\033[0;37m and \033[1;34meven integers\033[0;37m.\nTo start, please \033[1;32mpress any key.\033[0;37m\n")
print("===" * 50)

# Loading time
import time

time.sleep(0.5)
print("\33[31mGenerating your random list of integers.🥚")
time.sleep(1.0)
print("\n\33[35mPlease wait... 🐣")
time.sleep(1.0)
print("\n\33[33mGetting there.🐥\n")
time.sleep(1.0)
result = pyfiglet.figlet_format("Here's your list of integers:", font = "digital" )
print(result)
time.sleep(1.0)


# Open the numbers.txt (Append)
with open("numbers.txt", "a") as numbers_file:
# Generate 20 random integers.
    import random
    i = 0
    for i in range (20):
        integer = random.randint(1, 100)
        numbers_file.write(str(integer).center(70) + "\n")
        print(str(integer).center(40))
        i += 1
    print("\033[0;97m")
def procedure():
# Open number.txt (read), even.txt (append) and odd.txt (append)
    with open("numbers.txt") as numbers_file, open("even.txt", "a") as even_integer, open("odd.txt", "a") as odd_integer:
        result = pyfiglet.figlet_format("Here's your list of all even integers:", font = "digital" )
        even_integer.write(result)
        result = pyfiglet.figlet_format("Here's your list of all odd integers:", font = "digital" )
        odd_integer.write(result)
# Check every line in the number.txt.
        for line in numbers_file:
            integer = int(line)
# If even, append the integer to even.txt.
            if integer % 2 == 0:
                even_integer.write(str(integer).center(70) + "\n")
                print(integer , "is \033[0;34meven\033[0;97m".center(40))
# Else, if odd, append the integer to odd.txt.
            else:
                odd_integer.write(str(integer).center(70) + "\n")
                print(integer , "is \033[0;31modd\033[0;97m.".center(40))
# Run the procedure.
procedure()

print("\n\033[0;36mAll done, please check your files on your \033[0;35mdirectory. \033[0;36m'Till next sorting! 👩‍💻 \n")