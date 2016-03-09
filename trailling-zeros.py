#!/usr/bin/python
value = int(raw_input("Enter a value between 1 and 1000 :"))
while value < 1 or value > 1000:
	print "You have entered a invalid value"
	value = int(raw_input("Enter the a value between 1 and 1000 :"))
div = 5
initial_value = 0
while value > div:
	initial_value = initial_value + (value / div)
	div = div * 5
print  str(initial_value)
