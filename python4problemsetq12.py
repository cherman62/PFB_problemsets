#!/usr/bin/env python3
import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)
newlist = []
for num in range(num1,num2+1):
	if num%2==1:
		newlist.append(num)
print(newlist)
