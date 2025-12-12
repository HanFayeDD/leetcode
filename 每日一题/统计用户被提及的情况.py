from typing import List

MSG = "MESSAGE"
OFL = "OFFLINE"
ONL = "ONELINE"
interval = 60 

order = {MSG: 2,
         OFL: 1,
         ONL: 0}

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def parser(s:str):
            tmp = s.split(" ")
            r = []
            for ele in tmp:
                r.append(int(ele[2:]))
            return r
        cnt = [0] * numberOfUsers
        onlinels = []
        for ele in events:
            ## 处理数据
            ele[1] = int(ele[1])
            if ele[0] == MSG:
                if ele[2] != "ALL" and ele[2] != "HERE":
                    ele[2] = parser(ele[2])
            else:
                ele[2] = int(ele[2])
            ## 上线时间
            if ele[0] == OFL:
                newadd = [ONL, ele[1]+60, ele[2]]
                onlinels.append(newadd)
        events.extend(onlinels)
        events.sort(key= lambda x:[x[1], order[x[0]]])
        
        oneline = [True] * numberOfUsers
        
        for ele in events:
            if ele[0] == MSG:
                if ele[2] == "ALL":
                    cnt = [n+1 for n in cnt]
                elif ele[2] == "HERE":
                    cnt = [n+1 if oneline[idx] else n for idx, n in enumerate(cnt) ]
                else:
                    for n in ele[2]:
                        cnt[n] += 1
            elif ele[0] == OFL:
                oneline[ele[2]] = False
            else:
                oneline[ele[2]] = True      
        return cnt
        

if __name__ == "__main__":
    print(Solution().countMentions(numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))
    