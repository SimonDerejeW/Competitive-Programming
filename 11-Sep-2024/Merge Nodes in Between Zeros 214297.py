# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        temp = dummy

        while curr.next:
            if curr.val == 0:
                new_node = ListNode(0)
                temp.next = new_node
                temp = temp.next
            else:
                temp.val += curr.val
            curr = curr.next
        return dummy.next



