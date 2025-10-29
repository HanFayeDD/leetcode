class Solution:
    def smallestNumber(self, n: int) -> int:
        bs = bin(n)[2:]
        res = '1'*len(bs)
        return int(res, 2)

if __name__=="__main__":
    print(Solution().smallestNumber(5))