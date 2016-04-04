t = int(raw_input())
mylist = []
index = 0
loop = 0
while(loop < t):
	inputstring = raw_input()
	x, y, n =inputstring.split()
	x = int(x)
	y = int(y)
	n = int(n)
	while (index < x):
		mylist.append(y)
		index=index+1
	while(index < n):
		value = mylist[index-1]+mylist[index-2]+mylist[index-3]
		mylist.append(value)
		index = index + 1
	loop = loop + 1
	print(mylist[index - 1])
