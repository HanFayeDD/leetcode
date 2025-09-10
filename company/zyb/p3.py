import sys 

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))


maxcontain = -float('inf')
leftidx = 0
rightidx = n-1

while leftidx<rightidx:
    maxcontain = max(maxcontain, (rightidx - leftidx) * min(nums[leftidx], nums[rightidx]))
    
    if nums[leftidx] <= nums[rightidx]:
        leftidx += 1
    else:
        rightidx -= 1
        
print(maxcontain)
    
    
    
