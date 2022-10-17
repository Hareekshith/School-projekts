## Sequence one
for k in range(1, 6):
    print('*'*k, end="")
    print()


## Sequence two
for i in range(1, 6):
    for j in range(6-i):
        print(j+1, end=" ")
    print()

## Sequence three
for l in range(1, 6):
    for m in range(65, 65+l):
        print(chr(m), end=" ")
    print()