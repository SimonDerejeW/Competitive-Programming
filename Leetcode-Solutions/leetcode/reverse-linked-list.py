# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # temp1 = None
        
        # while curr and curr.next:
        #     temp = curr.next
        #     curr.next = temp1
        #     temp1 = curr
        #     curr = temp
        
        # return temp1
        
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev