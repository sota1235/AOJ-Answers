#!/usr/bin/python
# AOJ
# ALDS1_1_A
# 挿入ソート

n = int(input())
nums = list(map(int, input().split()))

for i in range(len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
    print(' '.join(map(str, nums)))
