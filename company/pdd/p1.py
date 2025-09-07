import sys

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, m = line1[0], line1[1] ## n item number; m 

line2 = sys.stdin.readline().strip()
price = list(map(int, line2.split()))

pricemod = [ele%m for ele in price]

# pricemod.sort()

d = dict()
cnt = 0

for num in pricemod:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for num in pricemod:
    if num != 0:
        target = m - num
        if target == num:
            if target in d:
                cnt += (d[target]-1)
        else:
            if target in d:
                cnt += d[target]
    
    else:
        target = 0
        if target in d:
            cnt += (d[target]-1)

print((cnt//2)%998244353)
        
    

