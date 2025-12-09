ranges = []
numbers = []
result = 0

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()

		if not line:
			continue

		if "-" in line:
			start, end = map(int, line.split("-"))
			ranges.append((start, end))
		else:
			numbers.append(int(line))


for n in numbers:
	for start, end in ranges:
		if start <= n <= end:
			result += 1
			break

print(result)