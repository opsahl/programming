import datetime as dt

date = dt.date(1901, 1, 1)
one_day = dt.timedelta(days = 1)

sundays = []

while date.year != 2001:
    if date.weekday() == 6:
        sundays.append(date)
    date += one_day

first_of_month_sundays = [sunday for sunday in sundays if sunday.day == 1]

print(len(first_of_month_sundays))
