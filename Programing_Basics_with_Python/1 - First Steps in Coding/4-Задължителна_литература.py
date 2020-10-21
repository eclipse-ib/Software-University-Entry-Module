current_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = (current_pages / pages_per_hour) / days
print(hours_per_day)
