# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = []
        curr = head
        while curr:
            pal.append(curr.val)
            curr = curr.next
        
        return pal == pal[::-1]

        