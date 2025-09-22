import sys 
from typing import List


def onegroup(nums:List[int]):
    maxsum = sum(nums)
    running = True
    while running:
        pass
            
        
        


n = int(sys.stdin.readline().strip())

res = []
for i in range(n):
    _ = sys.stdin.readline()
    nums = sys.stdin.readline().strip().split()
    nums = list(map(int, nums))
    oneres = onegroup(nums)
    res.append(oneres)
print(*res, sep="\n")