# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        def searcher(node, idx):
            if idx == len(arr):
                return True
            if not node:
                return False
            if node.val != arr[idx]:
                return False
            else:
                left = searcher(node.left, idx + 1)
                right = searcher(node.right, idx + 1)
                return left or right

        def dfs(node):
            if not node:
                return False
            
            if node.val == arr[0]:
                flag = searcher(node, 0)
                if flag:
                    return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
            
            

        result = dfs(root)
        return result