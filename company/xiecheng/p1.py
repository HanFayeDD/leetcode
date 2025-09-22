## 水仙花数
import sys 

n = str(sys.stdin.readline().strip())


leji = 0
for i in range(2, -1, -1):
    leji += int(n[i])**3

if leji == int(n):
    print("YES")
else:
    print("NO")