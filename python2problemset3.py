#!/usr/bin/env python3
import sys

value = sys.argv[1]
value = int(value)

if value <0:
    print("This value is negative")
elif value == 0:
    print("This value is 0")
elif value <50 and value%2 == 0:
    print("This value if even and less than 50")
elif value <50:
    print("This value is less than 50")
elif value >50 and value%3 == 0:
    print("This value is larger than 50 and divisible by 3")
elif value >50:
    print("This value is larger than 50")
else:
    print("This value is 50")

print("As a reminder, your input is", value)