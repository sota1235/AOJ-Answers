#!/usr/bin/python
# AOJ
# 0021

for i in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    if abs((y1 - y2) * (x3 - x4) - (y3 - y4) * (x1 - x2)) < 1.e-10:
        print('YES')
    else:
        print('NO')
