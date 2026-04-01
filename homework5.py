string = input("Enter something: ")
width = int(input())
symbol = input()
def corrector(string, width, symbol):
    print(f"{string:{symbol}^{width}}")
corrector(string=string, width=width, symbol=symbol)

import datetime
month_of_birthday = int(input("Enter the month of birthday: "))
day_of_birthday = int(input("Enter the day of birthday: "))
today = datetime.date.today()
year = today.year
date_now = datetime.datetime(year=year, month=month_of_birthday, day=day_of_birthday)
monday = "Monday"
tuesday = "Tuesday"
wednesday = "Wednesday"
thursday = "Thursday"
friday = "Friday"
saturday = "Saturday"
sunday = "Sunday"
for a in range(20):
    year += 1
    print(f"{year:=^80}")
    date_now = datetime.datetime(year=year, month=month_of_birthday, day=day_of_birthday)
    weekday = date_now.isoweekday()
    if weekday == 1:
        print(f"{monday:=^80}")
    if weekday == 2:
        print(f"{tuesday:=^80}")
    if weekday == 3:
        print(f"{wednesday:=^80}")
    if weekday == 4:
        print(f"{thursday:=^80}")
    if weekday == 5:
        print(f"{friday:=^80}")
    if weekday == 6:
        print(f"{saturday:=^80}")
    if weekday == 7:
        print(f"{sunday:=^80}")

import random
symbols = ["a", "b", "c", "d", "e"]
text = input("Enter something: ")
insert_position = random.randint(0, len(text))
random_symbol = random.choice(symbols)
text_with_symbol = text[:insert_position] + random_symbol + text[insert_position:]
print(text_with_symbol)