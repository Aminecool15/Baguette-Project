import random
import string
import os
import colorama

os.system("cls" if os.name == "nt" else "clear")

# Initialize colorama for Windows
colorama.init()

# Text to display
title = """
______                        _   _        ______          _           _    
| ___ \                      | | | |       | ___ \        (_)         | |   
| |_/ / __ _  __ _ _   _  ___| |_| |_ ___  | |_/ / __ ___  _  ___  ___| |_  
| ___ \/ _` |/ _` | | | |/ _ \ __| __/ _ \ |  __/ '__/ _ \| |/ _ \/ __| __| 
| |_/ / (_| | (_| | |_| |  __/ |_| ||  __/ | |  | | | (_) | |  __/ (__| |_  
\____/ \__,_|\__,_|\__,_|\___|\__|\__\___| \_|  |_|  \___/| |\___|\___|\__| 
              __/ |                                      _/ |               
             |___/                                      |__/               
"""

# Define colors for the gradient
colors = [colorama.Fore.BLUE, colorama.Fore.WHITE, colorama.Fore.RED]

def display_title():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console
    # Display the title with the gradient of colors
    for line in title.split('\n'):
        for i, character in enumerate(line):
            color = colors[i % len(colors)]
            print(color + character, end='')
        print(colorama.Style.RESET_ALL)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    display_title() # Display the title
    print("Choose an option: \n")
    print("1 - Generate a password")
    print("2 - Quit")
    choice = input()

    if choice == "1":
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print("\n" "Generated password: ", password, "\n")

        while True:
            answer = input("Do you want to use this password? (press F to confirm) ")
            if answer.lower() == "f":
                print("\n" "Please write it down somewhere: ", password, )
                break
            else:
                print("Are you dumb or what? I said press the F key. ")

        print(" ")
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

    print(" ")
