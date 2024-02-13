# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # curr = head
        # size = 1
        # if head is None:
        #     return
        
        # while curr.next:
        #     curr = curr.next
        #     size += 1
        
        # if size == 1:
        #     return head
        # tail = curr

        # current = head
        # prev = ListNode()

        # counter = 0
        # for i in range(size):
        #     if current.val >= x:
        #         prev.next = current.next
        #         current.next = None
        #         tail.next = current
        #         current = prev.next
        #         tail = tail.next
                
        #     else:
        #         if counter == 0:
        #             head = current
        #             counter += 1
        #         prev = current
        #         current = current.next
                

        # return head

        dummy1 = ListNode()
        dummy2 = ListNode()
        curr = head
        smaller = dummy1
        larger = dummy2

        while curr:
            if curr.val >= x:
                larger.next = curr
                larger = larger.next
                curr = curr.next
                larger.next = None
            else:
                smaller.next = curr
                smaller = smaller.next
                curr = curr.next
                smaller.next = None
        
        smaller.next = dummy2.next
        return dummy1.next