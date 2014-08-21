#!/usr/bin/python
# AOJ
# ALDS_1_1_B
# 最大公約数

a, b = map(int, input().split())
if a > b: a, b = b, a

while True:
    if b % a == 0:
        print(a)
        break
    else:
        b = b % a
        if a > b: a, b = b, a
