"""
birthday.py
Author: Payton
Credit: Andreas, Daniel, Avery, Ethan, Mr. Dennison, Feliz Hannukah
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]

n = input("Hello, what is your name? ")
m = input("Hi " + n + ", what was the name of the month you were born in? ")
y = float(input("And what year were you born in, " + n + "? "))
d = float(input("And the day? "))

if m in ["December", "January", "February"]:
    season = "winter"
elif m in ["March", "April", "May"]:
    season = "spring"
elif m in ["June", "July", "August"]:
    season = "summer"
elif m in ["September", "October", "November"]:
    season = "fall"

if y in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    type = "eighties"
elif y in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    type = "nineties"
elif y >= 2000:
    type = "two thousands"
elif y <= 1980:
    type = "Stone Age"

oct = month_name[October]

if month == m and todaydate == d:
    print("Happy Birthday!")
if oct == m and d == 31:
    print("Happy Halloween!")
else:
     print(  n + ", you are a " + season + " baby of the " + type + ".")
