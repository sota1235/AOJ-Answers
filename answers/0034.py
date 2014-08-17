#!/usr/bin/python
# AOJ
# 0034

while True:
    try:
        n = list(map(int, input().split(',')))
        v2, v1 = n.pop(), n.pop()
        dist = sum(n) * (v1 / (v1 + v2))
        total = 0
        ans = 0
        while total < dist:
            total += n[ans]
            ans += 1
        print(ans)
    except:
        break
