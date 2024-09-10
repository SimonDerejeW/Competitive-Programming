# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            x = math.gcd(curr.val, curr.next.val)
            new_node = ListNode(x)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = temp
        return head