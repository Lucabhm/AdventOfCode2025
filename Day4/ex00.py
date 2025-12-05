result = 0

def checkPos(list: list[str], x: int, y: int):
	dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1), (1, 0)]
	check = 0

	for dy, dx in dir:
		nowY = y + dy
		nowX = x + dx
		if (nowY >= 0 and nowY < len(list) and nowX >= 0 and nowX < len(list[y])):
			if list[nowY][nowX] == '@':
				check += 1
		if check >= 4:
			return True
	return False

with open('input.txt') as fd:
	list = fd.readlines()
	for y in range(0, len(list)):
		for x in range(0, len(list[y])):
			if list[y][x] == '@':
				if checkPos(list, x, y) == False:
					result += 1

print(result)