#!/usr/bin/python
# AOJ
# 0049

blood = [0] * 4

while True:
    try:
        b = input().split(',')[1]
        if b == 'A':
            blood[0] += 1
        elif b == 'B':
            blood[1] += 1
        elif b == 'AB':
            blood[2] += 1
        else:
            blood[3] += 1
    except:
        for b in blood: print(b)
        break
