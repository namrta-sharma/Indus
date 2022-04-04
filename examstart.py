# This program prints the exam date in dd/mm/yyyy format

# Prompt for user input

exam_st_date = input("Enter the start date for the exam(dd,mm,yyy): ")

# Use split function

myExam = exam_st_date.split(",")
day = myExam[0]
month=myExam[1]
year=myExam[2]

# Display the output

print("The examination starts from: ", day+"/"+month+"/"+year)
