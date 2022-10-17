print("Only Integers allowed")
num = int(input("Enter a number: "))
connum = str(num)
prodoffac = 1
sumofpowernum = 0
revnum = 0

# Perfect (Successful)
for i in range(1, num+1):
    if i%2 == 0:
        prodoffac *= i
if prodoffac == num:
    print("The number is perfect")
else:
    print("The number is not perfect")

# Armstrong (Successful)
for n in connum:
    sumofpowernum += int(n)**len(connum)
if sumofpowernum == num:
    print("The number is armstrong")
else:
    print("The number is not armstrong")

# Palindrome (Successful)
while num!=0:
    digits = num%10
    revnum = revnum*10 + digits
    num //= 10
if num == revnum:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")