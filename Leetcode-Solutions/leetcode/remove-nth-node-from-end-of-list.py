# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # def get_size():
        #     size = 0
        #     current = head
        #     while current:
        #         size += 1
        #         current = current.next
        #     return size
        # index = get_size()-n
        # if index == 0:
        #     head = head.next
        # count = 1
        # curr = head
        # while curr:
        #     if count == index:
        #         curr.next = curr.next.next
        #     curr = curr.next
        #     count+=1
        # return head

        def size():
            size = 0
            curr = head
            while curr:
                size += 1
                curr = curr.next
            return size
        idx = size() - n
        curr = head

        if idx == 0:
            head = head.next
            # return head
        count = 1
        while curr:
            if idx == count:
                curr.next = curr.next.next
            
            curr = curr.next
            count += 1
        
        return head

        






