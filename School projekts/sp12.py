list1 = [1,5,6,10,3]
maxnum = 0
minnum = 10000000000000000

for elements in list1:
    if maxnum < elements:
        maxnum = elements
for el in list1:
    if minnum > el:
        minnum = el

print("The maximum number is", maxnum)
print("The minimum number is", minnum)