import sys

def counttailzero(x):
    cnt = 0
    while x%10 == 0:
        cnt += 1
        x = x//10
    return x, cnt
    

n = int(sys.stdin.readline().strip())
nums = sys.stdin.readline().strip()
nums = list(map(int, nums.split()))

numsridzero = []
numsalreadycnt = []
for num in nums:
    a, b = counttailzero(num)
    numsridzero.append(a)
    numsalreadycnt.append(b)

    

print(sum(numsalreadycnt))


