x = float(input("Enter a number: "))
n = int(input("How many powers do yo wanna add the numbers to? "))
y = 0

for i in range(0, n+1):
    if i%2 == 0:
        y+=x**i
    elif i%2 == 1:
        y-=x**i
print(y)