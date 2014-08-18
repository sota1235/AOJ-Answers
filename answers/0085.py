#!/usr/bin/python
# AOJ
# 0085


while True:
    try:
        n, m = map(int, input().split(' '))
        pt = -1
        p_list = [i + 1 for i in range(n)]
        f_list = [0] * n
        while p_list.count(0) != n - 1:
            for i in range(m):
                if pt == n-1:
                    pt = 0
                else:
                    pt += 1
                while p_list[pt] == 0:
                    if pt == n-1:
                        pt = 0
                    else:
                        pt += 1
            p_list[pt] = 0
        print(sum(p_list))
    except:
        break
