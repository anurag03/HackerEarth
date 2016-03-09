testcase_value = int(raw_input())
j = 0
line = []
while j < testcase_value:
	x = raw_input()	
	line.append(x)
	j = j + 1
for value in line:
	value = value.split()
	count = len(value)
	loop_value = count/2
	count = count - 1
	i = 0
	while i < loop_value:
		value1 = value[i]
		value2 = value[count]
		value[i] = value2
		value[count] = value1
		i = i + 1
		count = count - 1
	req_value = ' '.join(value)
	print req_value
