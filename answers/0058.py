#!/usr/bin/python
# AOJ
# 0058

while True:
    try:
        xa, ya, xb, yb, xc, yc, xd, yd = map(float, input().split())
    except:
        break
    if abs((ya - yb) * (yc - yd) + (xa - xb) * (xc - xd)) < 1.e-10:
        print('YES')
    else:
        print('NO')
