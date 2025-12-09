ranges = []
merge = []
result = 0

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()

		if not line:
			continue

		if "-" in line:
			start, end = map(int, line.split("-"))
			ranges.append((start, end))


ranges.sort()

currStart, currEnd = ranges[0]

for start, end in ranges[1:]:
	if start <= currEnd + 1:
		currEnd = max(currEnd, end)
	else:
		merge.append((currStart, currEnd))
		currStart, currEnd = start, end

merge.append((currStart, currEnd))

result = sum(end - start + 1 for start, end in merge)
print(result)
