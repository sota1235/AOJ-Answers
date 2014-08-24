#!/usr/bin/python
# AOJ
# 0060

while True:
    try:
        c1, c2, c3 = map(int, input().split())
    except:
        break
    nums = list(set([i + 1 for i in range(10)]) ^ set([c1, c2, c3]))
    hit = 0
    for n in nums:
        if c1 + c2 + n <= 20: hit += 1

    if hit / 7 >= 0.5:
        print('YES')
    else:
        print('NO')
