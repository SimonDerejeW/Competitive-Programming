# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = []
        curr = ''
        for char in searchWord:
            ans = []
            curr += char
            idx = bisect.bisect_left(products, curr)
            for i in range(idx, idx + 3):
                if i < len(products) and products[i].startswith(curr):
                    ans.append(products[i])
            result.append(ans)
        return result
