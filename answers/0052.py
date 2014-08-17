# AOJ
# 0052
# python3

import math

while True:
	n = int(input())
	if n == 0: break
	fac = str(math.factorial(n))
	print(len(fac) - len(fac.rstrip('0')))