# This program prints out the colors which are present in color_list_1
# but not present/absent in color_list_2

# Ask user input for colors twice

color_list_1 = input("Please enter some set of colors: ")
color_list_2=input("Enter another set of colors: ")
color_list_1.split(",")
list1=color_list_1.split(",")
print(list1)
color_list_2.split(",")
list2=color_list_2.split(",")
print(list2)

# Display the output
for i in list1 or list2:
    if i not in list2:
        print(i)
