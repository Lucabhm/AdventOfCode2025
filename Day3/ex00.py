result = 0

with open('input.txt') as fd:
	for line in fd:
		nbr = 0
		for i in range(9, -1, -1):
			index = line.find(str(i))
			if index == -1 or index == len(line) - 2:
				continue
			else:
				nbr += i * 10
				for i in range(9, -1, -1):
					index2 = line[index + 1:].find(str(i))
					if index2 == -1:
						continue
					else:
						nbr += i
						result += nbr
						break
				break
print(result)
