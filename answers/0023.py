#!/usr/bin/python
# AOJ
# 0023

for i in range(int(input())):
    xa, ya, ra, xb, yb, rb = map(float, input().split(' '))
    ab_length = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    if ra > rb:
        max_r, min_r, min_c = ra, rb, 2
    else:
        max_r, min_r, min_c = rb, ra, -2

    if ab_length > ra + rb:
        ans = 0
    elif ab_length <= ra + rb:
        if ab_length + min_r < max_r:
            ans = min_c
        else:
            ans = 1
    print(ans)
