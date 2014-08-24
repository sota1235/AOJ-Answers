#!/usr/bin/python
# AOJ
# 0066

judge = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
        ]

while True:
    try:
        n = list(input())
        ans = None
        for j in judge:
            if n[j[0]] == n[j[1]] == n[j[2]]:
                if n[j[0]] == 's':
                    continue
                else:
                    ans = n[j[0]]
                    break
        if ans:
            print(ans)
        else:
            print('d')
    except:
        break
