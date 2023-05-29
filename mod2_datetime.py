# 2.Print the current date and time.

from datetime import date

today = date.today()

fav = today.strftime("%b-%d-%Y")

print("Today's date :", fav)