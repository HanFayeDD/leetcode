import sys 

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, tscore = line1[0], line1[1] ## 关卡数目、目标分数

slist = []
dlist = []


for i in range(n):
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    slist.append(line[0])
    dlist.append(line[1])

# print(slist)
# print(dlist)
left, right = 0, 0
period_score = 0
period_maxd = 0
period_maxd_idx = 0
all_mind = float('inf')
all_mind_idx = 0
while left < n and right < n+1:
    if period_score < tscore and right < n:
        period_score += slist[right]
        if dlist[right] >= period_maxd: ##question
            period_maxd = dlist[right]
            period_maxd_idx = right
        right += 1
    else:
        if right == n:
            if period_score >= tscore and period_maxd < all_mind:
                all_mind = period_maxd
                all_mind_idx = period_maxd_idx
                break

        if period_score >= tscore and period_maxd < all_mind:
            all_mind = period_maxd
            all_mind_idx = period_maxd_idx
        left = period_maxd_idx+1
        right = period_maxd_idx+1
        period_maxd_idx = period_maxd_idx+1
        period_score = 0
        period_maxd = 0


print(all_mind)
