#!/usr/bin/python
# AOJ
# 0100

while True:
    n = int(input())
    if n == 0: break

    data = {}
    staff = []
    for i in range(n):
        tmp = list(map(int, input().split(' ')))
        if tmp[0] in data:
            data[tmp[0]] += tmp[1] * tmp[2]
        else:
            data[tmp[0]] = tmp[1] * tmp[2]
            staff.append(tmp[0])

    if max(data.values()) < 1000000:
        print('NA')
    else:
        for k in staff:
            if data[k] >= 1000000:
                print(k)
