#!/usr/bin/python
# AOJ
# 0015

for i in range(int(input())):
    n1 = list(input())
    n2 = list(input())
    if len(n2) > len(n1):
        n1, n2 = n2, n1

    ans = []
    for i in range(len(n1)):
        a = int(ans.pop(0)) if len(ans) == i + 1 else 0
        c1 = int(n1.pop(-1))
        c2 = int(n2.pop(-1)) if len(n2) != 0 else 0
        ans = list(str(a + c1 + c2)) + ans
    if len(ans) > 80:
        print('overflow')
    else:
        print(''.join(ans))
