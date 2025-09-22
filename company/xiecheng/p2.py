import sys 

xiaoxie = []
subd = dict()
s = 'a'
for i in range(ord(s), ord(s)+26, 1):
    xiaoxie.append(chr(i))  
for i in range(len(xiaoxie)):
    subd[xiaoxie[i]] = xiaoxie[(i-1)%26]
daxie = []
daxied = dict()
s = 'A'
for i in range(ord(s), ord(s)+26, 1):
    daxie.append(chr(i))  
for i in range(len(daxie)):
    subd[daxie[i]] = daxie[(i+1)%26]
# print(subd)

_ = sys.stdin.readline()
s = sys.stdin.readline().strip()
# s = "bZ"

s_sub = ""
for ele in s:
    s_sub = s_sub + subd[ele]
# print(s_sub)

def onecheck(s, checkbeginidx):
    change = False
    for i in range(checkbeginidx, -1, -1):
        if i+1 >= len(s):
            continue
        if abs(ord(s[i])-ord(s[i+1])) == 32:
            change = True
            s = s[:i] + s[i+1:]
            return s, change, i  
    return s, change, -1
    
checkbeginidx = len(s_sub)-2
running = True
while running:
    s_sub, running, newidx = onecheck(s_sub, checkbeginidx)
    if running:
        checkbeginidx = newidx
print(s_sub)

    
    