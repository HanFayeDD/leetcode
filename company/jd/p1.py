import heapq
from typing import List
import sys

def onegroup(nums:List[int], k:int):
    q = []
    qdict = dict()
    for i in range(1, len(nums)):
        ele =  [-abs(nums[i]-nums[i-1]), i, nums[i]-nums[i-1]]
        heapq.heappush(q, ele)
        qdict[i] = ele
    
    for i in range(k):
        top = q[0]
        absvalfirst = -top[0]
        idx = top[1]
        noabsval = top[2]
        if noabsval > 0:
            top[2] = noabsval - 1
            top[0] = -abs(top[2])        
            if idx-1 in qdict:
                update = qdict[idx-1]
                update[2] = update[2]+1
                update[0] = -abs(update[2])
        elif noabsval < 0:
            top[2] = noabsval + 1
            top[0] = -abs(top[2])
            if idx + 1 in qdict:
                update = qdict[idx+1]
                update[2] = update[2] - 1
                update[0] = -abs(update[2])
        else:
            break
                
        heapq.heapify(q)
        
        absvalafter = -q[0][0]
        if absvalfirst < absvalafter:
            return absvalfirst
    return -q[0][0]
            
t = int(input())
res = []
for i in range(t):
    line = sys.stdin.readline().strip().split()
    line = list(map(int, line))
    n, k = line[0], line[1]
    numsls = sys.stdin.readline().strip().split()
    numsls = list(map(int, numsls))
    res.append(onegroup(numsls, k))
print(*res, sep="\n")
