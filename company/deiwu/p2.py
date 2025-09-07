import sys

line1 = sys.stdin.readline().strip()
line1 = list(map(int, line1.split()))
n, k = line1[0], line1[1]

dots = []
for i in range(n):
    tmp = sys.stdin.readline().strip()
    tmp = list(map(int, tmp.split()))
    dots.append((tmp[0], tmp[1]))

# print(dots)

visited = set() ## 一般 kval##bval  else x=val
res = 0

minval = 1e-8

def check1(target):
    global k
    global dots
    cnt = 0
    if k <= 2:
        return True
    for dot in dots:
        if dot[0] == target:
            cnt += 1
        if cnt >= k:
            return True
    return False

def check2(kval, bval):
    global k
    global dots
    cnt = 0
    if k <= 2:
        return True
    for dot in dots:
        if abs(kval * dot[0] + bval - dot[1])<=minval:
            cnt += 1
        if cnt >= k:
            return True
    return False

# if k == 1:
#     raise ValueError("tmp")


## k >= 2
for i in range(len(dots)):
    for j in range(i+1, len(dots)):
        ##  x=?
        keystr = ""
        if dots[i][0] == dots[j][0]:
            keystr = f"x={dots[i][0]}"
            if keystr not in visited:
                visited.add(keystr)
                # cnt = sum([ele[0] == dots[i][0] for ele in dots])
                # print(f"key:{keystr} val:{cnt}")
                if check1(dots[i][0]):
                    res += 1
        else:
            kval = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
            bval = dots[i][1] - kval * dots[i][0]
            # kval = round(kval, 10)
            # bval = round(bval, 10)
            keystr = f"k{kval}b{bval}"
            if keystr not in visited:
                visited.add(keystr)
                # cnt = sum([kval*ele[0] + bval == ele[1] for ele in dots])
                # print(f"key:{keystr} val:{cnt}")
                if check2(kval, bval):
                    res += 1
print(res)
            
        
            
            
