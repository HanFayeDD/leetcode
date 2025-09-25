from typing import List, Optional, Dict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next:Node = next
        self.random:Node = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_new_node_dict:Dict[Node, Node] = dict()
        cur = head
        while cur is not None:
            old_new_node_dict[cur] = Node(cur.val)
            cur = cur.next
            
        old = head
        while old is not None:
            new = old_new_node_dict[old]
            if old.next is None:
                new.next = None
            else:
                new.next = old_new_node_dict[old.next]
            if old.random is None:
                new.random = None
            else:
                new.random = old_new_node_dict[old.random]
            old = old.next
            
        return old_new_node_dict.get(head, None)

if __name__=="__main__":
    d = dict()
    d[None] = 1