# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        curr = head
        if head is None:
            return
        seen.add(curr.val)
        while curr and curr.next:
            seen.add(curr.val)
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
            
