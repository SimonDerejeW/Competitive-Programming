# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        size = 1
        node_left = ListNode()
        node_right = ListNode()

        curr = head
        while curr:
            if size == right + 1:
                node_left.next = curr
                curr = curr.next
                # node_left.next.next = None
            elif size == right:
                node_right.next = curr
                curr = curr.next
                # node_right.next.next = None
            else:
                curr = curr.next
            size += 1
        size = 1
        curr = head
        prev = node_left.next
        while curr:
            if size == left - 1:
                temp = curr.next
                curr.next = node_right.next
                curr = temp
            elif left <= size and right >= size:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                curr = curr.next
            size += 1
        if left == 1:
            return prev
        else:
            return head
            
            
