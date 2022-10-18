n = int(input("Enter a number: "))
n1 = int(input("Enter a number: "))
hcf = 1
lcm = 1

for i in range(1, n+1):
    if n%i == 0 and n1%i == 0:
        hcf = i
print(f"The HCF of {n} and {n1} is {HCF}")

lcm = n*n1/hcf

print(f"The LCM of {n} and {n1} is {LCM}")
