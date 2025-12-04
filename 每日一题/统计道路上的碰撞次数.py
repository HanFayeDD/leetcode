from typing import List


## 两个移动的相撞，碰撞次数+2，两辆都静止
## 一动一静相撞，碰撞次数+1，动的变静止

##碰撞的三种情况
## - 两个动的 + 2
## - 一动和一本来就是静的 + 1
## - 一动和本来动变为静的 + 1

class Solution:
    def countCollisions(self, directions: str) -> int:
        d = directions.lstrip("L")
        d = d.rstrip("R")
        return len(d) - d.count("S")