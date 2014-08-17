# AOJ
# 0071
# Python3

n = int(input())

for i in range(n):
	input()
	board = [list(input()) for i in range(8)]
	sx = int(input()) - 1
	sy = int(input()) - 1

	board[sy][sx] == 2
	bomb = []
	n_bomb = [[sy, sx]]
	points = []
	for j in range(len(board)):
		while '1' in board[j]:
			px = board[j].index('1')
			py = j
			points.append([py, px])
			board[j][px] = '2'
	
	while len(n_bomb) != 0:
		bomb += n_bomb
		n_bomb = []
		for b in bomb:
			for p in points:
				if (p[0] == b[0] and b[1]-3 <= p[1] <= b[1]+3) or (p[1] == b[1] and b[0]-3 <= p[0] <= b[0]+3):
					points.remove(p)
					n_bomb.append(p)
	
	ans = [['0'] * 8 for j in range(8)]
	for p in points:
		ans[p[0]][p[1]] = '1'

	print("Data %s:" % str(i+1))
	for p in ans:
		print("".join(p))