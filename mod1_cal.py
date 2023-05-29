# 1.Prompt user to enter year, month values and print the calender for the combination.
#         Hint: Refer to Calender module. 
import calendar

year = int(input("To get calendar of choice, enter year in format YYYY : "))
month = int(input("Next, enter month in format MM : "))

print(calendar.month(year, month))

