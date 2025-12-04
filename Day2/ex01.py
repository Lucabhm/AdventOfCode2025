result = 0

def splitStr(nbr, size):
	return [nbr[i:i + size] for i in range(0, len(nbr), size)]

with open('input.txt') as fd:
	input_file = fd.read()
	list = [s.strip() for s in input_file.split(',') if s.strip()]

	for r in list:
		start, end = map(int, r.split('-'))
		for i in range(start, end + 1):
			nbr = str(i)
			mid = len(nbr) // 2
			while (mid > 0):
				split = splitStr(nbr, mid)
				mid -= 1
				seen = set()
				seen.add(split[0])
				for s in split[1:]:
					if s not in seen:
						seen.add(s)
				if len(seen) == 1:
					result += i
					break

print(result)
