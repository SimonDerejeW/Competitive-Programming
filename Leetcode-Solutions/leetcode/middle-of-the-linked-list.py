# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def get_size():
        #     size = 0
        #     current = head
        #     while current:
        #         size += 1
        #         current = current.next
        #     return size
        # count = 0
        # mid = get_size()//2
        # curr = head
        # while curr:
        #     if count == mid:
        #         return curr
        #     curr = curr.next
        #     count+=1

        
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
        

