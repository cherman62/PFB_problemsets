#Question 4
count = 1
total = 0
while count <= 100:
    print(count)
    total = total+count
    count = count+1
print(total)

#Question 5
count = 1
factorial = 1
while count <= 10:
    factorial = factorial*count
    count +=1
print(factorial)

#Question 6
list6 = [101,2,15,22,95,33,2,27,72,15,52]
for item in list6:
    if item%2==0:
        print(item)

#Question 7
list7 = sorted(list6)
print(list7)
evenlist = []
oddlist = []
for sorteditem in list7:
    if sorteditem%2==0:
        evenlist.append(sorteditem)
    if sorteditem%2==1:
        oddlist.append(sorteditem)
print("Sum of even numbers:", sum(evenlist))
print("Sum of odds:", sum(oddlist))

#Question 8
for number in range(100):
    print(number)

for number2 in range(1,101):
    print(number2)

#Question 9
listq9 = [number for number in range(100)]
print(listq9)
list2q9 = [number for number in range(1,101)]
print(list2q9)

listforloopq9 = []
list2forloopq9 = []
for number in range(100):
    listforloopq9.append(number)
for number2 in range(1,101):
    list2forloopq9.append(number2)
print(listforloopq9)
print(list2forloopq9)

#Question 10 (I have this script as a standalone in another file called python4problemsetq10.py
#!/usr/bin/env python3
# import sys
# num1 = sys.argv[1]
# num2 = sys.argv[2]
# num1 = int(num1)
# num2 = int(num2)
# for num in range(num1+1,num2):
#     print(num)
# print("The minimum is:", num1)
# print("The maximum is:", num2)

#Question 11
#!/usr/bin/env python3
# import sys
# num1 = sys.argv[1]
# num2 = sys.argv[2]
# num1 = int(num1)
# num2 = int(num2)
# num_in_between = [number for number in range(num1, num2+1)]
# print(num_in_between)

#Question 12
# #!/usr/bin/env python3
# import sys
# num1 = sys.argv[1]
# num2 = sys.argv[2]
# num1 = int(num1)
# num2 = int(num2)
# newlist = []
# for num in range(num1,num2+1):
#         if num%2==1:
#                 newlist.append(num)
# print(newlist)


#Question 13
listdata = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for item in listdata:
    print(listdata.index(item),"\t",len(item),"\t",item)

listdatasorted = sorted(listdata, key=len, reverse=True)
for item in listdatasorted:
    print(item)