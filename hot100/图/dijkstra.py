# 初始化：
# 设置起点到自身的距离为 0，其他顶点为 ∞。
# 使用优先队列（最小堆）存储待处理的顶点，按距离排序。
# 迭代处理：
# 从队列中取出当前距离起点最近的顶点 u。
# 对 u 的每个邻居 v，检查是否需要松弛：
# 若 distance[u] + weight(u, v) < distance[v]，则更新 distance[v]。
# 终止条件：优先队列为空时结束。

# 应用场景：带权有向图或无向图中计算单源最短路径的经典算法，适用于边权重非负的情况
from typing import Dict, List
import heapq

def dijkstra(g:Dict[str, Dict[str, int]], start:str, allnode:List[str]):
    mindis:Dict[str, int|float] = dict()
    prevdict = dict()
    for node in allnode:
        mindis[node] = float('inf')
        prevdict[node] = None
    
    mindis[start] = 0
    hp = [(0, start)]
 
    
    
    while hp:
        dnow, nnow = heapq.heappop(hp)
        
        for n_neighbor, w in g[nnow].items():
            if mindis[n_neighbor] >= dnow + w:
                mindis[n_neighbor] = dnow + w 
                prevdict[n_neighbor] = nnow
                heapq.heappush(hp, (mindis[n_neighbor], n_neighbor))
    
    
    print(mindis)    
    for k, v in mindis.items():
        if v == float('inf'):
            print(f"can not reach {k} from {start}")
            continue
        running = True
        tmp = k
        while running:  
            print(tmp, end="")
            tmp = prevdict[tmp]
            if tmp is None:
                running = False
                print("")
                continue
            print(" < ", end="")
            
                
        
            


if __name__=="__main__":
    graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 1, 'D': 4},
        'C': {'A': 5, 'B': 1, 'D': 3},
        'D': {'B': 4, 'C': 3},
        'E': {}
    }
    dijkstra(graph, 'A', ['A', 'B', 'C', 'D', 'E'])
