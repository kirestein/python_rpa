from datetime import datetime as dt

date_time = dt.now()

day = date_time.day
month = date_time.month
year = date_time.year

hour = date_time.hour
minutes = date_time.minute
seconds = date_time.second

date = f'{day}/{month}/{year}'
time = f'{hour}:{minutes}:{seconds}'

print(f'{day}/{month}/{year}')
print(f'{hour}:{minutes}:{seconds}')