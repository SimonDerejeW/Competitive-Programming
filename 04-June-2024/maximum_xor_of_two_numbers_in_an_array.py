class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = 1 if (num & (1 << i)) else 0
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
        maxx = 0
        for num in nums:
            curr = self.root
            res = 0

            for i in range(31, -1, -1):
                bit = 1 if (num & (1 << i)) else 0

                if curr.children[1 - bit]:
                    res |= 1 << i
                    curr = curr.children[1 - bit]
                else:
                    curr = curr.children[bit]

            maxx = max(maxx, res)
            
        return maxx
