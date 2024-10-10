# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        print(nums)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        turn = 0
        idx = 0
        row, col = 0, 0

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n) and grid[row][col] == -1

        grid = [[-1 for i in range(n)] for j in range(m)]

        while idx != len(nums):
            grid[row][col] = nums[idx]

            idx += 1
            x, y = directions[turn]
            if inbound(row + x, col + y):

                row += x
                col += y
            else:
                if turn == 3:
                    turn = 0
                else:
                    turn += 1
                x, y = directions[turn]
                row += x
                col += y
        return grid
