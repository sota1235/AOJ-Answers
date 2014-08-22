#!/usr/bin/python
# AOJ
# 0047

b = {'A':1, 'B':0, 'C':0}

while True:
    try:
        n, m = input().split(',')
        b[n], b[m] = b[m], b[n]
    except:
        for i in b:
            if b[i] == 1: print(i)
        break
