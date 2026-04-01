import datetime

date_time = datetime.datetime(2021, 9, 27,
hour=12, minute=36, second=24, microsecond=585)
print(f"object datetime – {date_time}")
print(f"type – {type(date_time)}")

date_1 = datetime.date(2021,9,24)
time_1 = datetime.time(5,8,48)
print(f"date = {date_1}, type date = {type(date_1)}")
print(f"time = {time_1}, type time = {type(time_1)}")

date_now = datetime.datetime.now()
date_today = datetime.datetime.today()
date_date = datetime.date.today()
print(date_now)
print(date_today)
print(date_date)

date_now = datetime.datetime.now()
print(f"datetime to str = {date_now.strftime('%d.%m.%Y %H:%M')}")
date_str = "28/09/2021 11:20"
datetime_str_res = datetime.datetime.strptime(date_str,'%d/%m/%Y %H:%M')
print(f"str to datetime = {datetime_str_res}, type = {type(datetime_str_res)}")

date_now = datetime.datetime.now()
date = datetime.datetime(day=6, month=10, year = 1983)
print(date_now - date)