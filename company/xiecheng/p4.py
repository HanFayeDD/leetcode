import sys 

_ = sys.stdin.readline()
nums = sys.stdin.readline().strip().split()
nums = list(map(int, nums))

cnt = 0
for i in range(0, len(nums)-2):    
    for j in range(1, len(nums)-1):
        if nums[i] > nums[j]:
            cnt += 1
print(cnt)