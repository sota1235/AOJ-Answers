#!/usr/bin/python
# AOJ
# 0030

import itertools

while True:
    n, s = map(int, input().split(' '))
    if n + s == 0: break
    ans = 0
    for i in itertools.combinations(range(10), n):
        if sum(i) == s: ans += 1
    print(ans)
