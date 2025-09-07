import os
import sys

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

n, k = values[0], values[1]
sipt:str = sys.stdin.readline().strip()

lowercnt = 0
uppercnt = 0
for s in sipt:
    if s.isupper():
        uppercnt += 1

lowercnt = len(sipt) - uppercnt

## 原本无小写字母
if lowercnt == 0:
    if k % 2==0:
        print(uppercnt)
    else:
        print(uppercnt-1)
    exit()

## 原本有小写字母
if lowercnt >= k:
    print(uppercnt+k)
    exit()
elif lowercnt < k:
    kleft = k-lowercnt
    if kleft % 2 == 0:
        print(len(sipt))
    else:
        print(len(sipt)-1)


    




