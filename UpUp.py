s = raw_input()
s = s.split()
i = 0
string1 = " "
string = ""
for values in s:
	values = list(values)
	values[0] = values[0].upper()
	values = string.join(values)
	s[i] = values
	i = i + 1
s = string1.join(s)
print s 
