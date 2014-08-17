#!/usr/bin/python
# AOJ
# 0038

while True:
    try:
        cards = list(map(int, input().split(',')))
        cards.sort()

        if len(set(cards)) == 5:
            c = cards[0]
            if cards == [c, c+1, c+2, c+3, c+4]:
                print("straight")
            elif cards == [1,10,11,12,13]:
                print("straight")
            else:
                print("null")
        else:
            if len(set(cards)) == 2:
                t = cards.count(cards[0])
                if t == 1 or t == 4:
                    print("four card")
                else:
                    print("full house")
            elif len(set(cards)) == 3:
                flag = True
                i = 0
                while flag:
                    c = cards[i]
                    if cards.count(c) == 3:
                        print("three card")
                        flag = False
                    if cards.count(c) == 2:
                        print("two pair")
                        flag = False
                    i += 1
            else:
                print("one pair")
    except:
        break
