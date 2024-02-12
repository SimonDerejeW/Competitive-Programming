# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # lis = []
        # curr = list1
        # while curr:
        #     lis.append(curr.val)
        #     curr = curr.next
        # curr = list2
        # while curr:
        #     lis.append(curr.val)
        #     curr = curr.next
        # lis.sort()

        # if len(lis)!=0:
        #     new_head = ListNode(lis[0])
        #     curr = new_head
        #     for i in lis[1:]:
        #         newnode = ListNode(i)
        #         curr.next = newnode
        #         curr = curr.next
            
        #     return new_head
        # else:
        #     return None
        
        # merge = []
        # curr = list1
        # while curr:
        #     merge.append(curr.val)
        #     curr = curr.next
       
        # curr = list2
        # while curr:
        #     merge.append(curr.val)
        #     curr = curr.next
        
        # merge.sort()

        # merged_link = ListNode()
        # curr = merged_link
        # for i in merge:
        #     curr.next = ListNode(i)
        #     curr = curr.next
        
        # if merged_link.next:
        #     return merged_link.next
        # else:
        #     return
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

            
        if dummy.next:
            return dummy.next
        else:
            return

