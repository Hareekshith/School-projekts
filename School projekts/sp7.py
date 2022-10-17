num = int(input("Enter a number: "))
faclen = 0

for i in num:
    if num%i == 0:
        faclen += 1

if faclen ==2:
    print("Prime")
else:
    print("Composite")