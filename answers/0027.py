#!/usr/bin/python
# AOJ
# 0027

import datetime

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
        ]

while True:
    m, d = map(int, input().split(' '))
    if m == 0: break
    print(days[datetime.date(2004, m, d).weekday()])
