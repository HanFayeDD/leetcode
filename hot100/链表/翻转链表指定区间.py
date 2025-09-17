class Node():
    def __init__(self, val):
        self.val:int = val
        self.next:Node = None

def reverslink(first:Node, begin:int, end:int):
    head = Node(None)
    head.next = first
    
    p1 = head
    for i in range(begin-1):
        if p1.next is None:
            raise ValueError("link list length")
        p1 = p1.next
    
    pivot = p1.next    
    for i in range(end - begin):
        tmp = pivot.next
        if tmp is None:
            break
        pivot.next = tmp.next
        tmp.next = p1.next
        p1.next = tmp
        
    return head.next
        
        
def show(head:Node):
    now = head 
    while now is not None:
        print(now.val, end="**")
        now = now.next
    print("")
    
    
if __name__=="__main__":
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p6 = Node(6)
    p1.next = p2
    p2.next = p3 
    p3.next = p4 
    p4.next = p5 
    p5.next = p6
    show(p1)
    res = reverslink(p1, 1, 100)
    
    show(res)
    
            
    