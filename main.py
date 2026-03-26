# a python code basic for me to remember :3

# asks user for name
print ("What's your full name?")
username = input("")

# strips any whitespace from the inputted name
username = username.strip()

# Capiltizes name
username = username.title()

# checks if the inputted name is empty and prompts the user to enter a valid name
while username == "":
    print("Please enter a valid name.")
    username = input("")
    username = username.strip()

#Splits name into first and last name
first, last = username.split(" ")

# prints a greeting message with the inputted name
print("Hello, " + first + "! Welcome to the world!")

