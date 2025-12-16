arr = []
result = 0

with open('input.txt') as fd:
	for line in fd:
		line = line.strip()
		list = line.split(' ')
		list = [l for l in list if l]

		arr.append(list)

for i in range(0, len(arr[0])):
	tmp = int(arr[0][i])
	sign = arr[len(arr) - 1][i]
	for j in range(1, len(arr) - 1):
		if sign == '*':
			tmp *= int(arr[j][i])
		elif sign == '+':
			tmp += int(arr[j][i])
	result += tmp

print(result)