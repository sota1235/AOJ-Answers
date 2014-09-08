#!/usr/bin/python

while True:
    x = float(input())
    h = float(input())
    if x + h == 0: break
    S = 0
    a = ((x / 2) ** 2 + h ** 2) ** 0.5
    S += x * x
    S += (a * x * 0.5) * 4
    print(S)
