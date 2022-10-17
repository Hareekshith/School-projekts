print("only integers are allowed")
num = int(input("Enter a number: "))
factors = list()
alldigitsofnumber = list(map(int, f"{num}"))
alldigitofnumberrv = alldigitsofnumber.copy()
alldigitofnumberrv.reverse()
numcheck = list()
sum = 0
n = 0 #just for armstrong

opmode = int(input("""
1. Check your number is a perfect number
2. Check your number is a Armstrong number
3. Check your number is a palindrome
"""
))

if(opmode == 1): ## Perfect
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)
    for numbers in factors:
        sum += numbers
    if (sum-num) == num:
        print("The number is perfect")
    else:
        print("The number is not perfect")
elif(opmode == 2): ## Armstrong
    for i in alldigitsofnumber:
        sum += i**len(alldigitsofnumber)
    if num == sum:
        print("The number is armstrong")
    else:
        print("The number is not armstrong")
elif(opmode == 3): ## Palindrome
    if(alldigitsofnumber ==  alldigitofnumberrv):
        print("The number is a palindrome")
    else:
        print("Nah, no palindrome valindrome, go do your work")
else:
    print("ERROR!!!!!!!!!!!")