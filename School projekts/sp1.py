n1 = float(input("Enter a number: "))
n2 = float(input("Enter a number: "))
n3 = float(input("Enter a number: "))

print("From the three numbers you entered, the largest is")

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
elif n3 > n2 and n3 > n3:
    print(n3)

