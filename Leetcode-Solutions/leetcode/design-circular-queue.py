class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = None
        self.tail = None
        

    def enQueue(self, value: int) -> bool:
        if self.count == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = self.head             
            self.count += 1
            return True
        elif self.count < self.k:
            new_node = ListNode(value)
            self.tail.next = new_node
            self.tail = self.tail.next
            self.count += 1
            return True
        else:
            return False


    def deQueue(self) -> bool:
        if self.head:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.count -= 1
            
            if self.count == 0:
                self.tail = None
            return True
               
         
        return False
    def Front(self) -> int:
        if self.head:
            return self.head.val
        return -1
        

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()