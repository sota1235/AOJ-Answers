#!/usr/bin/python
# AOJ
# 0045

price, num, c = 0, 0, 0

while True:
    try:
        p, n = map(float, input().split(','))
        price += p * n
        num += n
        c += 1
    except:
        print(int(price))
        num /= c
        s = str(num).split('.')
        if int(s[1][0]) > 4:
            print(int(num) + 1)
        else:
            print(int(num))
        break
