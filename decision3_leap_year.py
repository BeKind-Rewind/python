# 3.Prompt user to enter a year and print out if it is a leap year or not.

year = int(input("To determine if it's a leap year, enter a 4 digit year > 1500 :"))

if year % 400 == 0 :
  print("Heck yeah! It's a leap year!")
elif year % 100 == 0 :
  print("Awww... It's not a leap year!")
elif year % 4 == 0 :
  print("Heck yeah! It's a leap year!")
else :
  print("Awww... It's not a leap year")