result = 0

with open('input.txt') as fd:
	input_file = fd.read()
	list = [s.strip() for s in input_file.split(',') if s.strip()]

	for r in list:
		start, end = map(int, r.split('-'))
		for i in range(start, end + 1):
			nbr = str(i)
			mid = len(nbr) // 2
			left = nbr[:mid]
			right = nbr[mid:]
			if left == right:
				result += i

print(result)
