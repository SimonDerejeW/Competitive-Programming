# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None
# class MyLinkedList:

#     def __init__(self):
#         self.head = None
        

#     def get(self, index: int) -> int:
#         count = 0
#         curr = self.head
#         while curr != None:
#             if count == index:
#                 return curr.val
#             curr = curr.next
#             count+=1
#         return -1

#     def addAtHead(self, val: int) -> None:
#         newnode = ListNode(val)
#         newnode.next = self.head
#         self.head = newnode
        

#     def addAtTail(self, val: int) -> None:
#         newnode = ListNode(val)
#         if self.head==None:
#             self.head = newnode
#             return
#         curr = self.head
#         while curr.next!=None:
#             curr = curr.next
#         curr.next = newnode

        

#     def addAtIndex(self, index: int, val: int) -> None:
#         newnode = ListNode(val)
#         curr = self.head
#         if index == 0:
#             newnode.next = self.head
#             self.head = newnode
#             return
#         count = 1
#         while curr:
#             if count == index:
#                 temp = curr.next
#                 curr.next = newnode
#                 newnode.next = temp
#             curr = curr.next
#             count+=1

        

#     def deleteAtIndex(self, index: int) -> None:
#         if index == 0 and self.head:
#             self.head = self.head.next
#             return

#         count = 0
#         curr = self.head
#         while curr and curr.next:
#             if count == index - 1:
#                 curr.next = curr.next.next
#                 return
#             curr = curr.next
#             count += 1
        
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList():
    def __init__(self):
        self.head = None
        
    
    def addAtHead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    
    def get(self, index):
        count = -1
        head = self.head
        while head:
            count += 1
            if count == index:
                return head.val
            head = head.next
        return -1
        
    
    def addAtTail(self, new_data):
        if self.head is None:
            self.addAtHead(new_data)
            return

        new_node = Node(new_data)
        head = self.head
        
        while head.next:
            head = head.next
        
        head.next = new_node

    
    def addAtIndex(self,index,new_data):
        if index == 0:
            self.addAtHead(new_data)
            return

        count = 0
        head = self.head
        new_node = Node(new_data)

        while head:
            
            if count == index - 1:
                new_node.next = head.next
                head.next = new_node
            head = head.next
            count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
            return

        count = 0
        curr = self.head
        while curr and curr.next:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)