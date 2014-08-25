#!/usr/bin/python
# AOJ
# ALDS1_5_A
# Case10でTime Limit Exceeded

import itertools

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
M = list(map(int, input().split()))

for m in M:
    ans = 'no'
    for i in range(1, n + 1):
        for c in itertools.combinations(A, i):
            #print(c)
            if sum(list(c)) == m:
                ans = 'yes'
    print(ans)
