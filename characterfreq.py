# This program prints out the number of characters in a string

# Ask for user input for a string
def char():

    myString = input("Please enter a string: ")
    myString.split(" ")
    String1=myString.split(" ")

# Calculate the number of characters in the string
    ch1=0
    for chr in String1:
        ch1=ch1+len(chr)
    print(ch1)
char()
