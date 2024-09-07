# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def dfs(root):
            nonlocal arr
            if root is None:
                return
            if root.children is None:
                return
            for node in root.children:
                dfs(node)
            arr.append(root.val)
        dfs(root)
        return arr