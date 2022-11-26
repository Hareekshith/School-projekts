list1 = list()
numel = int(input("Enter the number of elements: "))

for i in range(numel):
    list1.append(int(input("Enter the element: ")))

max = list1[0]  
min = list1[0]  
for elements in list1:
    if max < elements:
        max = elements
for el in list1:
    if min > el:
        min = el

print("The maximum number is", max)
print("The minimum number is", min)