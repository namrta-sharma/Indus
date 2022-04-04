# This program prints a list of numbers

# Prompt for user input

num = eval(input("Enter numbers separated by commas: "))

# Initialize vairables

list = str(num.split(","))

# For loop

for i in list:
    list.append(i*i)
