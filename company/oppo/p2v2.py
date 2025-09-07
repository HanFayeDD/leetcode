## pass

import sys

nums = sys.stdin.readline().strip()
nums = list(map(int, nums.split()))
n, x, y = nums[0], nums[1], nums[2]

nums = sys.stdin.readline().strip()
nums = list(map(int, nums.split()))

target = x ^ y


needset = set()
flag = False
for num in nums:
    needtmp = target - num
    if needset < 0:
        continue
    if needtmp in needset:
        flag = True
        break
    needset.add(num)


if flag:
    print("Yes")
else:
    print("No")



    
