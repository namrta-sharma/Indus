# This program prints the date in month, day and year format

# Prompt for user input

dateStr = input("Enter the date(mm/dd/yyyy): ")

# Split the date into month, day and year strings
myDate = dateStr.split("/")
monthStr = myDate[0]
dayStr = myDate[1]
yearStr = myDate[2]

# Convert the month, day and year into ints

monthStr = int(monthStr)
dayStr = int(dayStr)
yearStr = int(yearStr)

# Create a list for all the months

months = ("January","February","March","April","May","June","July","August","September","October","November","December")

# Derive the month string to the month number

monthStr = months[int(monthStr - 1)]

# Print the date

print("The date is: ", str(monthStr), str(dayStr)+",", str(yearStr ))
