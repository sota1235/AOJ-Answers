#!/usr/bin/python
# AOJ
# 0062

while True:
    try:
        nums = list(map(int, list(input())))
    except:
        break
    while len(nums) > 1:
        tmp = []
        for i in range(len(nums)-1):
            tmp.append(int(str(nums[i] + nums[i+1])[-1]))
        nums = [] + tmp
    print(nums[0])
