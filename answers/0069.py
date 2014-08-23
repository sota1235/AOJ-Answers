#!/usr/bin/python
# AOJ
# 0069

def solver(n, s, g, amida):
    for a in amida:
        a = list(map(int, list(a)))
        r, l = 0, 0
        if s != 1:
            l = a[s-2]
        if s != n:
            r = a[s-1]

        if r == 1:
            s += 1
        elif l == 1:
            s -= 1

    return True if s == g else False

while True:
    n = int(input())
    if n == 0: break
    s = int(input())
    g = int(input())
    d = int(input())
    amida = [input() for j in range(d)]
    if solver(n, s, g, amida):
        print(0)
    else:
        ans = None
        for i in range(d):
            for j in range(n-1):
                a = amida[i]
                if a[j] == '0':
                    a = a[:j] + '1' + a[j+1:]
                    if '11' in a:
                        continue
                    else:
                        if solver(n, s, g, amida[:i] + [a] + amida[i+1:]):
                            ans = str(i+1) + ' ' + str(j+1)
                            break
            if ans: break
        if ans:
            print(ans)
        else:
            print(1)
