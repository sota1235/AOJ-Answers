#!/usr/bin/python
# AOJ
# 0024

while True:
    try:
        n = float(input())
        ans = 1
        v = 0
        while v < n:
            ans += 1
            y = ans * 5 - 5
            t = (y / 4.9) ** 0.5
            v = 9.8 * t
        print(ans)
    except:
        break
