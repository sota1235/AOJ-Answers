#!/usr/bin/python
# AOJ
# 0065

old = []
new = []
ans = []
t = True

while True:
    try:
        n = input()
    except:
        break

    n = n.split(',')[0]
    if not n:
        t = False
    if t:
        old.append(n)
    else:
        new.append(n)

for o in set(old):
    if o in new:
        s = old.count(o) + new.count(o)
        ans.append([int(o), int(s)])
ans.sort()
for a in ans:
    print('%d %d' % (a[0], a[1]))
