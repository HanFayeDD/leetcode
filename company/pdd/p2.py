import sys 

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, x = line1[0], line1[1]

line2 = sys.stdin.readline().strip()
clist = list(map(int, line2.split()))

consume = []

for idx, c in enumerate(clist):
    staydays = n - idx 
    consume.append(staydays * c)

consume.sort()

cnt = 0
xleft = x
for num in consume:
    if num <= xleft:
        cnt += 1
        xleft -= num
    else:
        break

print(cnt)