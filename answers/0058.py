#!/usr/bin/python
# AOJ
# 0058

# TODO:http://manapedia.jp/text/index?text_id=647

def slant(xa, ya, xb, yb):
    if ya - yb == 0:
        return 'y'
    elif xa - xb == 0:
        return 'x'
    else:
        return (ya - yb) / (xa - xb)

while True:
    try:
        xa, ya, xb, yb, xc, yc, xd, yd = map(float, input().split())
    except:
        break
    AB = slant(xa, ya, xb, yb)
    CD = slant(xc, yc, xd, yd)
    lines = [AB, CD]
    is_digit = 'x' not in lines and 'y' not in lines

    if lines == ['x', 'y'] or lines == ['y', 'x']:
        print('YES')
        continue

    if is_digit:
        print('YES' if AB * CD == -1 else 'NO')
    else:
        print('NO')
