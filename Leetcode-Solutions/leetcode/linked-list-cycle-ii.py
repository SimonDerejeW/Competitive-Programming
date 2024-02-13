# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        inter = ListNode()
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                inter.next = fast
                break
        
        if flag is False:
            return
        curr = head
        
        while curr:
            if curr == inter.next:
                return curr
            
            curr = curr.next
            inter.next = inter.next.next
            

            
                