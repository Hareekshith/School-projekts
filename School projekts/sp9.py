n = int(input("Enter a number: "))
n1 = int(input("Enter a number: "))
factors = list()
factors1 = list()
HCF = list()
LCM = list()

for i in range(1, n+1):
    if n%i==0:
        factors.append(i)

for i1 in range(1, n1+1):
    if n1%i1 == 0:
        factors.append(i1)

for i in factors:
    if i in factors1:
        HCF.append(i)

for i in range(1, n*n1+1):
    if i%n==0 and i%n1==0:
        LCM.append(i)

print("HCF: ", sum(HCF))
print("LCM: ", sum(LCM))