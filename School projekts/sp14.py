numel = int(input("Enter the number of elements: "))
list = list()


for i in range(0, numel):
    list.append(int(input("Enter the element: ")))

print(list)
selnum = int(input("Enter the element which needs to be searched for: "))


for j in list:
    if j == selnum:
        print("The element is found at index: ", list.index(j))
        print("The element is found at position: ", list.index(j)+1)
        break
    elif selnum not in list:
        print("Element not found")
        break