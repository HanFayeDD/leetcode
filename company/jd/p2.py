import sys 

mod = 998244353

n_s = sys.stdin.readline().strip()
m = int(sys.stdin.readline().strip())
limit = None
d = dict()
for i in range(m):
    line = sys.stdin.readline().strip().split()
    line = list(map(int, line))
    # limit.append(line)
    if line[0] not in d:
        d[line[0]] = line[1]
    else:
        if d[line[0]] != line[1]:
            print(0)
            exit()
limit = list(d.items())
limit = [ele for ele in limit if ele[0] <= len(n_s)-1]

allbyweishu = (2**(len(n_s)-len(limit)))%mod
print(allbyweishu)


    
    