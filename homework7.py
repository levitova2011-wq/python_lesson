import datetime
month_of_birthday = int(input("Enter the month of birthday: "))
day_of_birthday = int(input("Enter the day of birthday: "))
today = datetime.date.today()
year = today.year
date_now = datetime.datetime(year=year, month=month_of_birthday, day=day_of_birthday)
for a in range(20):
    year += 1
    print(year)
    date_now = datetime.datetime(year=year, month=month_of_birthday, day=day_of_birthday)
    weekday = date_now.isoweekday()
    if weekday == 1:
        print("Monday")
    if weekday == 2:
        print("Tuesday")
    if weekday == 3:
        print("Wednesday")
    if weekday == 4:
        print("Thursday")
    if weekday == 5:
        print("Friday")
    if weekday == 6:
        print("Saturday")
    if weekday == 7:
        print("Sunday")
name_of_file = input("Enter the name of this file: ")
text = input("Enter the text: ")
file = open(f"{name_of_file}.txt", "w")
file.write(f"{text}\n{datetime.datetime.today()}")
file.close()