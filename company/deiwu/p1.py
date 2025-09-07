import sys

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, k = line1[0], line1[1] ## nums length; wndwidth

line2 = sys.stdin.readline().strip()
nums = list(map(int, line2.split()))
# 10 3
# 5 5 5 10 10 10 5 10 10 10
periodnum = n - k + 1
periodsum = None
periodmaxsum = -float('inf')
maxsumbeginidx = None
for i in range(periodnum):
    beginidx = i
    endidx = i + k - 1
    # print(f"{beginidx}-{endidx}")
    if periodsum is None:
        periodsum = sum(nums[beginidx:endidx+1])
    else:
        periodsum = periodsum - nums[beginidx-1]
        periodsum = periodsum + nums[endidx]
        
    if periodsum > periodmaxsum:
        # print(periodsum)
        periodmaxsum = periodsum
        maxsumbeginidx = beginidx

        
print(maxsumbeginidx + (k//2) + 1)