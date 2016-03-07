a = int(raw_input())
s = raw_input()
s = s.split()
s = s[:a]
i = 0
ans = ""
for value in s:
	s[i] = int(value)
	i = i + 1
for value in s:
	check = 0
	for values in s:
		flag = value % values
		if (flag == 0):
			check = check + 1
	if check == 1:
		ans = ans + " " + str(value)
print ans
