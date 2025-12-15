class Solution:
    def numberOfWays(self, corridor: str) -> int:
        SIT = "S"
        PLANT = "P"
        MOD = 10**9 + 7 
        left = None
        right = None
        res = 1
        n = len(corridor)
        for i in range(n):
            if corridor[i] == PLANT:
                continue
            if left is None:
                left = i 
                continue
            if right is None:
                right = i 
                continue
            
            # 迎新来的是新组的第一个
            if left < right:
                res *= (i-right)
                res %= MOD
                left = i 
            # 迎来的是新租的第二个
            elif left > right:
                right = i 
        
        # 一组都凑不到
        if left is None or right is None:
            return 0 
        
        # 有一个落单
        if left > right:
            return 0
        
        return res 
        
                
        
        

## pass，但解决空间复杂度的问题
class Solution1:
    def numberOfWays(self, corridor: str) -> int:
        SIT = "S"
        PLANT = "P"
        MOD = 10**9 + 7 
        snum = 0 
        groupls = []
        group = []
        n = len(corridor)
        for i in range(n):
            if corridor[i] == SIT:
                if len(group) == 0:
                    group.append(i)
                else: 
                    group.append(i)
                    groupls.append(group)
                    group = [] 
            else:
                continue 
        
        ## 两个判断条件有交集
        if len(group) != 0 or len(groupls) == 0:
            return 0 
        
        
        ## len(groupls)>=1 也能得到正确结果
        res = 1
        for i in range(1, len(groupls)):
            res *= (groupls[i][0] - groupls[i-1][1])
            res %= MOD

        return res 
    
    
if __name__ == "__main__":
    print(Solution().numberOfWays(corridor = "SSPPSPS"))
                    
            
            
            
            
                    
        
                    