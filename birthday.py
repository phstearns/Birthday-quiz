"""
birthday.py
Author: Payton
Credit: Andreas
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

n = input("Hello, what is your name? ")
m = input("Hi " + n + ", what was the name of the month you were born in? ")
y = float(input("And what year were you born in, " + n + "? "))
d = float(input("And the day? "))

if m in ["December", "January", "February"]:
    season = ("winter")
elif m in ["March", "April", "May"]:
    season = ("spring")
elif m in ["June", "July", "August"]:
    season = ("summer")
elif m in ["September", "October", "November"]:
    season = ("fall")
print(season)

if y is [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    type = ("eighties")
elif y>= 1990 or y<= 1999:
    type = ("nineties")
elif y>= 2000:
    type = ("two thousands")
elif y<= 1980:
    type = ("Stone Age")
print(type)