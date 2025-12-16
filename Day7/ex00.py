arr = []
result = 0

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()
		arr.append(list(line))

def findChar(arr: list, x: int, y: int):
	stack = [(x, y)]

	while stack:
		x, y = stack.pop()

		if not (0 <= x < len(arr[0]) and 0 <= y < len(arr)):
			continue

		if arr[y][x] == '^':
			stack.append((x - 1, y))
			stack.append((x + 1, y))
		else:
			if arr[y][x] != '|':
				arr[y][x] = '|'
				stack.append((x, y + 1))

findChar(arr, 70, 0)

for j in range(0, len(arr)):
	for i in range(0, len(arr[j])):
		if arr[j][i] == '^' and arr[j - 1][i] == '|':
			result += 1

for line in arr:
	print(line)


print(result)