# This program adds 'ing' to the end of a given string if len(str)>=3
# and if the string already ends with an 'ing', it adds 'ly' to the end of the str
# If the len(str)<3 then it leaves the str unchanged

# Ask for a string from the user
def string():
    myString = input("Please enter a string: ")
    myString.split(" ")
    String1=myString.split(" ")

# Use if statements
    if len(String1)>=3:
        print(myString+"ing")
    elif myString[-3:]=="ing" or len(String1)>=3:
        print(myString+"ly")
    elif len(String1)<3:
        print(myString)
string()
