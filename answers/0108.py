#!/usr/bin/python
# AOJ
# 0108

while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = list(map(int, input().split(' ')))

    times = 0
    old_nums = [-1] * n
    while old_nums != s:
        new_nums = []
        for i in s:
            new_nums.append(s.count(i))
        old_nums = s[::]
        s = new_nums[::]
        times += 1
    print(times - 1)
    print(' '.join(map(str, s)))
