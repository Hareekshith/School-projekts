x = int(input("Enter a number: "))
n = int(input("Enter the power of the number till you want your numbers to get added: "))
c = 0
y = 1
for a in range(x):
    y = y*(a+1) ##correct

for b in range(n+1):
    c += (x**b)/y
print(c+1)
