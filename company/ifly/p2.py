import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

dleft = dict()
dright = dict()

## init dleft
dleft[values[0]] = 1

## init dright
for ele in values[1:]:
    if ele not in dright:
        dright[ele] = 1
    else:
        dright[ele] += 1

maxpower = -float('inf')
for i in range(0, n-1):
    leftdistinct = len(dleft)
    rightdistinct = len(dright)
    maxpower = max(maxpower, leftdistinct+rightdistinct)

    nextnum = values[i+1]
    ## update left
    if nextnum in dleft:
        dleft[nextnum] += 1
    else:
        dleft[nextnum] = 1

    ## update right
    nextnumcnt = dright[nextnum]
    if nextnumcnt > 1:
        dright[nextnum] -= 1
    elif nextnumcnt == 1:
        del dright[nextnum]
    else:
        raise ValueError()
    
print(maxpower)


