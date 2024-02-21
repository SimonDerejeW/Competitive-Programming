# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        curr = head
        size = 0

        while curr:
            curr = curr.next
            size += 1
        
        if size > k:
            parts = size % k
        else:
            parts = 0
        length = size // k

        curr = head

        while curr:
            res.append(curr)

            for _ in range(length- 1):
                curr = curr.next
            
            if parts:
                curr = curr.next
                parts -= 1
            
            temp = curr.next
            curr.next = None
            curr = temp
    
        while size < k:
            res.append(None)
            k -= 1
        return res


       

        
