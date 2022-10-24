list = list()
f = 0
numofelements = int(input("Enter the number of elements(only even): "))

for k in range(0, numofelements):
    list.append(int(input("Enter the element: ")))

for j in list:
    print(j, end=" ")
print("\n")

for i in list:
    f = list.index(i)
    if f%2 == 0:
        print(list[f+1], end = " ")
    elif f%2 == 1:
        print(list[f-1], end = " ")