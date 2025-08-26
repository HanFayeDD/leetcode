from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minlen = float('inf')
        maxlen = -float('inf')
    
        hashset = set(wordDict)

        for ele in hashset:
            minlen = min(minlen, len(ele))
            maxlen = max(maxlen, len(ele))
            
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(dp)):
            for l in range(minlen, maxlen+1):
                dpstartidx = i - l + 1
                dpendidx = i 
                if dpstartidx < 1:
                    continue
                if dp[dpstartidx-1] and s[(dpstartidx-1):(dpendidx-1+1)] in hashset:
                    dp[dpendidx] = True
               
        print(' '+s)
        print(dp)
        return dp[-1]

if __name__=="__main__":
    print(Solution().wordBreak("catsandog",  ["cats","dog","sand","and","cat"]))