from typing import List

# - 两种操作都是可逆的，做两次等于没做
# - 两种操作只能交替进行、要不然路径不是最短的
# - 把最高位变为0的方法只有从将其变成1100....000才可以

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = n.bit_length()
        
        return 2**k - 1 - self.minimumOneBitOperations(n - 2**(k-1))


if __name__=="__main__":
    print(Solution().minimumOneBitOperations(6))