from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            hashval = self.calhash(s)
            if hashval not in d:
                d[hashval] = [s]
            else:
                d[hashval].append(s)
        
        return list(d.values())

    def calhash(self, s:str):
        l = list(s)
        l.sort()
        return "".join(l)