# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # print(size)
        if size % 2 != 0 or size == 2:
            curr = head
            while curr.next:
                curr = curr.next
            tail = curr
            
            curr = head
            for _ in range((size // 2)):
                tail.next = curr.next
                curr.next = curr.next.next
                curr = curr.next
                tail = tail.next
                tail.next = None
        else:
            curr = head
            while curr.next and curr.next.next:
                curr = curr.next
            tail = curr
            curr = head
            while curr.next:
                curr = curr.next
            tail2 = curr
            # print(tail)
            # print(tail2)
            curr = head
            for _ in range((size // 2) - 1):
                tail.next = curr.next
                curr.next = curr.next.next
                curr = curr.next
                tail = tail.next
                tail.next = None
                # print(curr)
            
            curr = head
            while curr.next:
                curr = curr.next
            # tail2.next = None
            curr.next = tail2
            # print(tail2)
        
        return head
            
            

        
        