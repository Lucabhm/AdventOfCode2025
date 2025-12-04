import re

result = 0
check = 50

with open('input.txt') as pares_file:
	for line in pares_file:
		nbr = int(re.search(r"\d{1,2}$", line).group())
		fullNbr = int(line[1:])
		if (fullNbr > 100):
			result += int(fullNbr / 100)
		tmp = check
		if line[0] == 'R':
			check += nbr
			if check >= 100:
				check -= 100
				if tmp != 0:
					result += 1
				continue
		else:
			check -= nbr
			if check < 0:
				check += 100
				if tmp != 0:
					result += 1
				continue
		if check == 0:
			result += 1

print(result)