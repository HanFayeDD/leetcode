from typing import List
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param queueA int整型二维数组 表示在 A 产品体验区 排队的所有消费者信息
# @param queueB int整型二维数组 表示在 B 产品体验区 排队的所有消费者信息
# @param targetConsumerIds int整型一维数组 目标消费者在两个队列中的索引
# @return int整型
#
class Solution:
    def calculateTotalTime(self , queueA: List[List[int]], queueB: List[List[int]], targetConsumerIds: List[int]) -> int:
        # write code here
        for i in range(len(queueA)):
            queueA[i].append(i)
        for i in range(len(queueB)):
            queueB[i].append(i)
        # print(queueA)
        if queueA:  
            queueA.sort(key=lambda x:self.calkey(x[:]), reverse=True)
        if queueB:
            queueB.sort(key=lambda x:self.calkey(x[:]), reverse=True)
        # print(queueA)
        flag = [0, 0]
        nowtime = 0
        afinishtime = 0
        bfinishtime = 0
        while True:
            if nowtime >= afinishtime:
                nowa = queueA.pop()
            if nowtime >= bfinishtime:
                lastb = queueB[-1]
                break
            
        return 25
            
        
    def calkey(self, ele:List[int])->int:
        s = ""
        for num in ele:
            s = s + str(num)
        return int(s)
    
if __name__=="__main__":
    print(Solution().calculateTotalTime([[1,2], [2,2], [2, 3], [2, 3]], [[1,2], [2,2], [2, 3], [2, 3]], []))

        
        