from datetime import datetime
import time
now = datetime.now()
row_format = "Current date and time: %Y, %m, %d, %H:%M:%S"
row_format1 = "Current year: %Y"
row_format2 = "Month if year: %B"
row_format3 = "Week number of the year: %W"
row_format4 = "Weekday of the week: %w"
row_format5 = "Day of year: %j"
row_format6 = "Day of the month: %d"
row_format7 = "Day of week: %A"
print(time.strftime(row_format))
print(time.strftime(row_format1))
print(time.strftime(row_format2))
print(time.strftime(row_format3))
print(time.strftime(row_format4))
print(time.strftime(row_format5))
print(time.strftime(row_format6))
print(time.strftime(row_format7))