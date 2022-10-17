x = float(input("Enter a number: "))
n = int(input("How many powers do yo wanna add the numbers to? "))
y = 0

for i in range(1, n+1):
    y += (x**i)

print(y+1)