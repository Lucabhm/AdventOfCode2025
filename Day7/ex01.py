from functools import lru_cache

arr = []
result = 0

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()
		arr.append(list(line))

@lru_cache(None)
def findChar(x: int, y: int):
	global arr

	if not (0 <= x < len(arr[0]) and 0 <= y < len(arr)):
		return 1

	if arr[y][x] == '^':
		return findChar(x - 1, y) + findChar(x + 1, y)
	else:
		return findChar(x, y + 1)

result = findChar(70, 0)

print(result)