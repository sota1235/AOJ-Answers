#!/usr/bin/python
# AOJ
# 0016

import math

degree = 90
x = 0
y = 0

while True:
    a, b = map(int, input().split(','))
    if a is 0 and b is 0: break
    x += a * math.cos(math.radians(degree))
    y += a * math.sin(math.radians(degree))
    degree -= b
    if degree > 360:
        degree -= 360
    elif degree < 0:
        degree += 360
print(int(x))
print(int(y))
