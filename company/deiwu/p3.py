import sys

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, m = line1[0], line1[1]

tmp = sys.stdin.readline().strip()
als = list(map(int, tmp.split())) ##积分

tmp = sys.stdin.readline().strip()
ccls = list(map(int, tmp.split())) ## 通过关卡数
## 失败积分不变 cnt变为0

tmp = sys.stdin.readline().strip()
bls = list(map(int, tmp.split()))

cb_dict = dict()
for k, v in zip(ccls, bls):
    cb_dict[k] = v 
    
print(cb_dict)

dp = [[], []]

## cnt leijiscore
dp[0].append([1, als[0]])
dp[1].append([0, 0])

for i in range(1, len(als)):
    

