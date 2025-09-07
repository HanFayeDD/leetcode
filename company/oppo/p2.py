import sys

nums = sys.stdin.readline().strip()
nums = list(map(int, nums.split()))
n, x, y = nums[0], nums[1], nums[2]

nums = sys.stdin.readline().strip()
nums = list(map(int, nums.split()))

target = x ^ y

flag = False

nums.sort()

if nums[-1] + nums[-2] < target:
    print("No")
    exit()

for i in range(n-1):
    if nums[i] + nums[-1] < target:
        continue
    for j in range(i+1, n):
        if nums[i] + nums[j] > target:
            break
        if nums[i] + nums[j] == target:
            flag = True
            break


if flag:
    print("Yes")
else:
    print("No")


