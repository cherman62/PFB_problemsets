value = 54

if value <0:
    print("this value is negative")
elif value <50 and value%2 == 0:
    print("this value if positive, even and less than 50")
elif value <50:
    print("this value is less than 50")
elif value >50 and value%3 == 0:
    print("this value is positive, larger than 50 and divisible by 3")
elif value >50:
    print("this value is positive")
else:
    print("this value is 50")