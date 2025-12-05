result = 0

def checkPos(list: list[str], x: int, y: int):
	dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1), (1, 0)]
	check = 0

	for dy, dx in dir:
		nowY = y + dy
		nowX = x + dx
		if (nowY >= 0 and nowY < len(list) and nowX >= 0 and nowX < len(list[y])):
			if list[nowY][nowX] == '@' or list[nowY][nowX] == 'x':
				check += 1
		if check >= 4:
			return True
	return False

with open('input.txt') as fd:
	listStr = fd.readlines()
	grid = [list(row) for row in listStr]
	while True:
		tmp = 0
		for y in range(0, len(grid)):
			for x in range(0, len(grid[y])):
				if grid[y][x] == '@':
					if checkPos(grid, x, y) == False:
						grid[y][x] = 'x'
						tmp += 1
		if tmp == 0:
			break
		result += tmp
		for y in range(0, len(grid)):
			for x in range(0, len(grid)):
				if grid[y][x] == 'x':
					grid[y][x] = '.'

print(result)