'''To create a fibonacci sequence'''
reqd = int(input('Enter the length of the sequence: '))
n = 1
pn = 0
        
for i in range(reqd - 1):
    pn = n + pn
    n = pn +  n
    print(f"{pn}, {n}", end=', ')