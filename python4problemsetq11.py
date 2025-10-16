#!/usr/bin/env python3
import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)

num_in_between = [number for number in range(num1,num2+1)]
print(num_in_between)

