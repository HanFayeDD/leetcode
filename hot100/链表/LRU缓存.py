from typing import Dict

class ListNode():
    def __init__(self, key:int=-1, val:int=-1):
        self.key = key
        self.val = val
        self.prev:ListNode = None
        self.next:ListNode = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d:Dict[int, ListNode] = dict()
        self.capacity = capacity
        self.size = 0
        self.emptyhead = ListNode()
        self.emptytail = ListNode()
        self.emptyhead.next = self.emptytail
        self.emptytail.prev = self.emptyhead

    def get(self, key: int) -> int:
        res = self.d.get(key, None)
        if res is None:
            return -1 
        self.moveToHead(res)
        return res.val
    
    def put(self, key: int, value: int) -> None:
        ## 存在
        if key in self.d:
            ## 清除旧的哈希表和双向链表
            self.delByNode(self.d[key])
            del self.d[key]
            ## 添加至于哈希表与新的至头部
            newnode = ListNode(key=key, val=value)
            self.d[key] = newnode
            self.addToHead(newnode)
        ## 不存在
        else:
            ## 容量可以直接塞
            if self.size < self.capacity:
                newnode = ListNode(key=key, val=value)
                self.d[key] = newnode
                self.addToHead(newnode)
                self.size += 1
            ## 容量不够删除末尾再添加
            else:
                delnode = self.emptytail.prev
                self.delByNode(delnode)
                del self.d[delnode.key]
                
                newnode = ListNode(key=key, val=value)
                self.d[key] = newnode
                self.addToHead(newnode)

    def delByNode(self, node:ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node:ListNode):
        node.next = self.emptyhead.next
        self.emptyhead.next.prev = node 

        self.emptyhead.next = node
        node.prev = self.emptyhead


    def moveToHead(self, node:ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.emptyhead.next
        self.emptyhead.next.prev = node

        self.emptyhead.next = node
        node.prev = self.emptyhead


if __name__=="__main__":
    obj = LRUCache(2)
    obj.put(2,1)
    obj.put(2,2)
    print(obj.get(2))
    obj.put(1,1)
    obj.put(4,1)
    print(obj.get(2))
    
        
