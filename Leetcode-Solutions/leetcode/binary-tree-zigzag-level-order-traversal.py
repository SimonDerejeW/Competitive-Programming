# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root , level):
            nonlocal res
            if root is None:
                return

            if level < len(res):
                res[level].append(root.val)
            else:
                res.append([root.val])

            bfs(root.left,level + 1)

            bfs(root.right, level + 1)

        bfs(root,0)
        for idx in range(len(res)):
            if idx % 2 != 0:
                res[idx] = reversed(res[idx])
        return res