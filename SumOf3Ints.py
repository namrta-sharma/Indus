# This program prints the sum of 3 integers
# And if two of the integers entered are equal then the sum=0

# Ask user to enter the input integers

int1= int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer:"))
int3 = int(input("Enter the third integer: "))


# Create if statements
sum = 0
if int1==int2 or int2==int3 or int3==int1:
    print(sum)
else:
    sum = sum + int1+int2+int3
    print(sum)
