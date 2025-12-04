result = 0

def findNbr(line: str, start: int, rest: int):
	for i in range(9, -1, -1):
		index = line[start:].find(str(i))

		if index == -1:
			continue

		pos = start + index
		if len(line) - pos < rest:
			continue

		start = pos + 1
		rest -= 1
		return i, start, rest
	return None, start, rest

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()
		nbr = 0
		start = 0
		rest = 12

		for i in range(0, 12):
			tmp, start, rest = findNbr(line, start, rest)
			if tmp is not None:
				nbr = nbr * 10 + tmp
		result += nbr

print(result)
