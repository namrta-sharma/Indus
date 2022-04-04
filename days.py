# Ask user for dates

date1 = input("Enter the date(yyyy,mm,dd): ")
date1.split(",")
myList1=date1.split(",")
date2= input("Enter the date(yyyy,mm,dd): ")
date2.split(",")
myList2=date2.split(",")
# Formula
day1=myList1[2]
day2=myList2[2]
day1=int(day1)
day2=int(day2)
diff=day2-day1
# Display the number of days
print(diff, "days")

