# 3.Write a python program to calculate no.of days between 2 dates.
#         Sample dates: (2014,7,2) , (2014, 7, 11)
#         Expected output: 9 days

from datetime import date as date_n  
dInputM1 = int(input("To find number of days between two dates, enter first date's MM:"))
dInputD1 = int(input("First date's DD:"))
dInputY1 = int(input("First date's YYYY:"))

dInputM2 = int(input("Now, enter second date's MM:"))
dInputD2 = int(input("second date's DD:"))
dInputY2 = int(input("secdon date's YYYY:"))

def num_days(date1, date2) :
  return (date2 - date1).days

date1 = date_n(dInputY1, dInputM1, dInputD1)  
date2 = date_n(dInputY2, dInputM2, dInputD2)  
print ("Number of Days between the given Dates are: ", num_days(date1, date2), "days")  
