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
m = input("Hi " + n + " , what was the name of the month you were born in? ")
y = float(input("And what year were you born in, " + n + "? "))
d = float(input("And the day? "))
January = 1
February = 2
March = 3 
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9
October = 10
November = 11
December = 12

if m == "December" or m == "January" or m == "February":
    season = "winter"
elif m == "March" or m == "April" or m == "May":
    season = "spring"
elif m == "June" or m == "July" or m == "August":
    season = "summer"
else m == "September" or m == "October" or m == "November":
    season = "fall"
"""    
if y>= 1980 or y<= 1989:

if y>= 1990 or y<= 1999:

if y>= 2000:

if y<= 1980:

"""