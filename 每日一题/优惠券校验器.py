from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def check_code(s)->bool:
            if s is None or len(s) == 0:
                return False

            nonlocal asic_code
            for ss in s:
                if ord(ss) not in asic_code:
                    return False
                
            return True
        
        asic_code = set()
        for i in range(ord("a"), ord("z")+1):
            asic_code.add(i)
            
        for i in range(ord("A"), ord("Z")+1):
            asic_code.add(i)
            
        for i in range(ord("0"), ord("9")+1):
            asic_code.add(i)
            
        asic_code.add(ord("_"))
        
        res = []
        
        businesstype = ("electronics", "grocery", "pharmacy", "restaurant")
        businessorder = {
            "electronics":0,
            "grocery":1,
            "pharmacy":2,
            "restaurant":3
        }
        
        n = len(code)
        
        for i in range(n):
            if not isActive[i]:
                continue
            if not check_code(code[i]):
                continue
            if businessLine[i] not in businesstype:
                continue
            res.append([businessLine[i], code[i]])
        # print(res)
        res.sort(key= lambda x:[businessorder[x[0]], x[1]])
        res = [ele[1] for ele in res]
        return res 
        
        
if __name__ == "__main__":
    print(Solution().validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True]))
        
            