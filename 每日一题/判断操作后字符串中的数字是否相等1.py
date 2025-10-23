class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            tmps = ''
            for i in range(len(s)-1):
                tmps += str((int(s[i])+int(s[i+1]))%10)
            s = tmps
        
        return s[0] == s[1]
    
if __name__=="__main__":
    print(Solution().hasSameDigits('34789'))