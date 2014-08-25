#!/usr/bin/python
# AOJ
# 0057

while True:
    try:
        n = int(input())
    except:
        break
    ans = 2
    for i in range(2, n + 1):
        ans += i
    print(ans)
