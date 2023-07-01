import sys

m, d = map(int, sys.stdin.readline().split())

weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day_sum = 0
days_in_month = 0
for i in range(1, m):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif i in [4, 6, 9, 11]:
        days_in_month = 30
    else: #2월인 경우
        days_in_month = 28
    day_sum = day_sum + days_in_month

day_sum+= d

print(weekday[day_sum % 7])