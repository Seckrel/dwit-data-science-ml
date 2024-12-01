import datetime
import nepali_datetime

dt = datetime.date(2024, 11, 14)
nt = nepali_datetime.date.from_datetime_date(dt)
print(dt)
new_nt = nepali_datetime.datetime.strptime(str(nt), format="%K")