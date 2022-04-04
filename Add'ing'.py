# This program adds 'ing' to the end of a given string if len(str)>=3
# and if the string already ends with an 'ing', it adds 'ly' to the end of the str
# If the len(str)<3 then it leaves the str unchanged

# Ask for a string from the user
def str():
    myString = input("Please enter a string: ")
    
    str=list(myString)

# Use if statements
    if len(str)>=3:
        if str[-3]=="i" and str[-2]=="n" and str[-1]=="g":
            print(myString+"ly")
        else:
            print(myString+"ing")
    elif len(str)<3:
        print(myString)
str()
