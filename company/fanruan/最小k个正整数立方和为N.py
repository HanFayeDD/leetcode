# 链接：https://www.nowcoder.com/questionTerminal/4bc284dc9d0144628a722eb5d1191ef3?answerType=1&f=discussion
# 来源：牛客网

# 给出一个数字N（0<N<1000000）,将N写成立方数和的形式，求出需要的最少立方数个数。
# 例如N=17，1+8+8 = 17，最少需要3个立方数，则输出3。
# N= 28,1+1+1+1+8+8+8=28, 需要7个立方数，1+27=28,需要2个立方数，所以最少立方数为2，则输出2。


# 那就是可以轻松确定拓扑序的问题，例如线性模型，都是从左往右进行转移，区间模型，一般都是从小区间推导到大区间。自底向上的一个经典实现是斐波那楔数列的递推实现
# ，即F[i] = F[i - 1] + F[i -2]。
# dp[t]  = min(dp[t], dp[t - i * i * i] + 1);


## 写法1
def cal(N:int)->int:
    dp = [float('inf')]*(N+1)
    dp[0] = 0 ## 这里0要初始化，参考dp[1] = min(dp[1], dp[1-1**3]+1) = 1
    for nown in range(1, N+1):
        for i in range(1, nown):
            if nown-i**3 >= 0:
                dp[nown] = min(dp[nown], dp[nown - i**3]+1)
    return dp[-1]


## 写法2更优雅
def cal1(N: int) -> int:
    if N == 0:
        return 0
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # 初始化dp[0]
    for nown in range(1, N + 1):
        max_i = int(nown ** (1/3)) + 1  # 计算i的上界
        for i in range(1, max_i + 1):
            cube = i ** 3
            if cube <= nown:
                dp[nown] = min(dp[nown], dp[nown - cube] + 1)
    return dp[N]



if __name__=="__main__":
    print(cal(28))