#!/usr/bin/python
# AOJ
# ALDS1_5_A

def branch(array, b, p, m):
    if p == len(array):
        return m == sum(array[i] for i in range(p) if b[i] == 1)

    b2 = b[:p] + [0] + b[p+1:]
    r = branch(array, b, p+1, m)
    l = branch(array, b2,  p+1, m)
    if r or l:
        return True
    else:
        return False

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
M = list(map(int, input().split()))

for m in M:
    b = [1] * n
    print('yes' if branch(A, b, 0, m) else 'no')
