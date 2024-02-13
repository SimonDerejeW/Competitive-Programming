# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        currB = headB
        # arr_A =[]
        # arr_B = []
        # while curr:
        #     arr_A.append(curr)
        #     curr = curr.next

        # while currB:
        #     arr_B.append(currB)
        #     currB = currB.next

        # size = min(len(arr_A), len(arr_B))
        # x = arr_A
        # y = arr_B
        # if len(arr_A) > len(arr_B):
        #     x = arr_B
        #     y = arr_A


        # for i in range(size):
        #     if x[i] in y:
        #         return x[i]

        # rightA = len(arr_A) - 1
        # rightB = len(arr_B) - 1

        # while rightA >= 0 and rightB >= 0:
        #     if arr_A[rightA] != arr_B[rightB]:
        #         if rightA == len(arr_A) - 1:
        #             return 
        #         return arr_A[rightA + 1]
        #     rightA -= 1
        #     rightB -= 1

        ##O(N)
        # dicA = {}

        # while curr:
        #     dicA[curr] = curr.val
        #     curr = curr.next
        
        # while currB:
        #     if currB in dicA:
        #         return currB
        #     currB = currB.next

        sizeA = 0
        sizeB = 0

        while curr:
            sizeA += 1
            curr = curr.next
        while currB:
            sizeB += 1
            currB = currB.next

        curr = headA
        currB = headB
        while sizeA > sizeB:
            if curr == currB:
                return curr
            sizeA -= 1
            curr = curr.next

        
        while sizeA < sizeB:
            if curr == currB:
                return curr
            sizeB -= 1
            currB = currB.next

        
        while curr:
            if curr == currB:
                return curr
            curr = curr.next
            currB = currB.next
        
        
        


        