# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        mask = 0
        prefix = [0]
        for num in arr:
            mask ^= num
            prefix.append(mask)

        answer = []
        for left, right in queries:
            curr = prefix[left] ^ (prefix[right + 1])
            answer.append(curr)
        return answer

        
