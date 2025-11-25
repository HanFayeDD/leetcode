## 时间慢
class Solution1:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1 
        
        res = 1 
        bit = 1
        
        while res % k != 0:
            res = 10 * res + 1
            bit += 1 
            
        return bit
    
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1 % k
        for i in range(1, k + 1):
            if n == 0:
                return i
            n = (n * 10 + 1) % k
        return -1
    
# 现在我们来分析这个过程：

# 我们计算 rem_1, rem_2, rem_3, ... 这个余数序列。

# 这些余数的值，都必须在 {0, 1, 2, ..., k-1} 这个集合里。

# 如果我们在计算过程中，找到了余数 0，那么我们就找到了答案。

# 关键点：如果我们在计算了 k 次之后（即计算了 rem_1 到 rem_k），仍然没有找到余数 0，会发生什么？

# 这意味着我们生成的 k 个余数 rem_1, rem_2, ..., rem_k 全都是非零的。
# 非零的可能余数只有 k-1 个，即 {1, 2, ..., k-1}。
# 现在，我们有 k 个“鸽子”（rem_1 到 rem_k），但只有 k-1 个“非零鸽巢”（1 到 k-1）。
# 根据抽屉原理，必然至少有一个余数重复了。
# 一旦余数重复，就会进入一个死循环。

# 假设 rem_i = rem_j，其中 i < j。
# 那么下一步的余数 rem_{i+1} = (rem_i * 10 + 1) % k。
# 而 rem_{j+1} = (rem_j * 10 + 1) % k。
# 因为 rem_i = rem_j，所以必然有 rem_{i+1} = rem_{j+1}。
# 同理，rem_{i+2} = rem_{j+2}，以此类推。
# 这意味着余数序列从 rem_i 开始进入了一个循环 (rem_i, rem_{i+1}, ..., rem_{j-1})。

if __name__ == "__main__":
    print(Solution().smallestRepunitDivByK(2))