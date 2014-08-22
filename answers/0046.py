#!/usr/bin/python
# AOJ
# 0046

m = []

while True:
    try:
        m.append(float(input()))
    except:
        print(max(m) - min(m))
        break
