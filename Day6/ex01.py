arr = []
count = []
result = 0
tmpStr = []

with open('input.txt') as fd:
	input_file = fd.readlines()

	lastLine = input_file[len(input_file) - 1]


i = 0
while i < len(lastLine):
	if lastLine[i] == '*' or lastLine[i] == '+':
		i += 1
		continue
	start = i
	while i < len(lastLine) and lastLine[i] == ' ':
		i += 1

	if i == len(lastLine):
		i += 1
	count.append(i - start)

for line in input_file:
	i = 0
	pos = 0
	test = []
	while i < len(count):
		test.append(line[pos: pos + count[i]])
		pos += count[i] + 1
		i += 1
	arr.append(test)

for i in range(len(arr[0]) - 1, -1, -1):
	sign = arr[len(arr) - 1][i][0]
	if (sign == '*'):
		tmp = 1
	else:
		tmp = 0
	for k in range(3, -1, -1):
		tmpStr = ""
		if len(arr[0][i]) - 1 >= k:
			tmpStr += arr[0][i][k]
		for j in range(1, len(arr) - 1):
			if len(arr[j][i]) - 1 >= k:
				tmpStr += arr[j][i][k]

		if tmpStr == '':
			continue
		if (sign == '*'):
			tmp *= int(tmpStr)
		elif (sign == '+'):
			tmp += int(tmpStr)
	result += tmp

print(result)
