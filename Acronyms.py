# This program prints the acronym for a string entered by the user

# Ask for a string from the user

myString = input("Please enter a string: ")
myString.upper()
word1=myString.upper()
word1.split(" ")
words = word1.split(" ")

# Create a for loop
ch1=''
for chr in words:
    ch1=ch1+chr[0]

# Display the output
print(ch1)
    
    

