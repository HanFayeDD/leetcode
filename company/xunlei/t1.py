#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 节点数（节点编号从 `0` 开始）
# @param s int整型 源节点编号
# @param t int整型 目标节点编号
# @param node_bandwidths int整型一维数组 每个节点的可用带宽数组，索引i对应节点i的带宽
# @param edges int整型二维数组 边数信息，从左到右分别为：起点节点编号、终点节点编号、链路剩余带宽、传输延迟
# @param d int整型 需传输的数据量  
# @return int整型
#
from typing import List
class Solution:
    def find_min_delay_path(self , n: int, s: int, t: int, node_bandwidths: List[int], edges: List[List[int]], d: int) -> int:
        # write code here
        usedn = set()
        for i in range(n):
            if node_bandwidths[i] >= d:
                usedn.add(i)
        if len(usedn) == 0:
            return -1
        
        usededage = []
        for i in range(len(edges)):
            if edges[i][0] not in usedn or edges[i][1] not in usedn or edges[i][2] < d:
                continue
            else:
                usededage.append(edges[i])
        if len(usededage) == 0:
            return -1
        
        dp = [[float('inf')]*n for i in range(n)]
        
        for ele in usededage:
            dp[ele[0]][ele[1]] = ele[3]
            
        mindix = float('inf')
        stack = []
        visited = set()
        stack.append(s)
        
        while 