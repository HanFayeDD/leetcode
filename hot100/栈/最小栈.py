## 方法1: 可行
### 栈中元素是一个二元组，为（val，min_val）
## 方法2: 不可行
### self.stack = []记录原始val、self.currtopdiffmin记录当前top和最小值的diff。
### 在pop操作时候，还是需要全部遍历更新self.currtopdiffmin
## 方法3: 可行
### self.val_min = []记录val与未添加val时候的min的差值。self.min记录当前最小值
### push时，方便
### pop时， 更新self.min方便
### top时， 通过val_min以及self.min可以得到top
#### 可不可以是self.val_min = []记录val与添加val之后的min的差值。self.min记录当前最小值
#### 不行。[]都是0笑死
## 方法4: 不可行
### self.mindiff存储历史时期的相邻min的差值，self.min记录当前最小值
### push时候，方便
### top还原不了val

## 方法3
class MinStack:

    def __init__(self):
        self.val_lastmin = []
        self.curmin = float("inf")

    def push(self, val: int) -> None:
        # 第一个元素
        if not self.val_lastmin:
            self.val_lastmin.append(None)
            self.curmin = val
            return
        
        # 不是第一个元素
        # self.val_min = []记录val与未添加val时候的min的差值。self.min记录当前最小值
        if val <= self.curmin:
            self.val_lastmin.append(val-self.curmin)
            self.curmin = val
        else:
            self.val_lastmin.append(val-self.curmin)
            self.curmin = self.curmin

    def pop(self) -> None:
        pop_ele = self.val_lastmin.pop()
        ## 只有一个元素还pop了
        if pop_ele == None:
            self.curmin = float('inf')
            return

        ## 更新curmin
        ### pop出去了最小值
        ### 上一个最小值是更小的
        if pop_ele < 0:
            self.curmin = self.curmin - pop_ele
        else:
            self.curmin = self.curmin



    def top(self) -> int:
        if len(self.val_lastmin)==1 and self.val_lastmin[0] == None:
            return self.curmin
        
        top_ele = self.val_lastmin[-1]
        ## 当前top值不是当前最小值
        if top_ele > 0:
            return top_ele + self.curmin
        else:
            return 0 + self.curmin

    def getMin(self) -> int:
        return self.curmin



## 方法2 不可行
class MinStackV2:
    def __init__(self):
        self.stack = []
        self.currtopdiffmin = None

    def push(self, val: int) -> None:
        if self.currtopdiffmin == None:
            self.currtopdiffmin = val
        else:
            if len(self.stack) == 1:
                beforemin = self.stack[-1]
            else:    
                beforemin = self.stack[-1] - self.currtopdiffmin
            aftermin  = min(beforemin, val)
            self.currtopdiffmin = val - aftermin    
        self.stack.append(val)

    def pop(self) -> None:
        beforemin = self.stack[-1] - self.currtopdiffmin
        popval = self.stack[-1]
        self.stack.pop()
        
        if len(self.stack) == 0:
            self.currtopdiffmin = None
            return
        
        ## 弹出的不等于最小值
        if popval != beforemin:
            return
        
        ## 是否有更多最小值
        morebeforemin = False
        for ele in self.stack:
            if ele == beforemin:
                morebeforemin = True
                break
        
        ### 有更多最小值
        if morebeforemin:
            return
        
        ### 无更多最小值
        aftermin = min(self.stack)
        self.currtopdiffmin = self.stack[-1] - aftermin
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-1] - self.currtopdiffmin
    
