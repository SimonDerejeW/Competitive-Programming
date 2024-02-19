class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # counts = []
        # for i in range(len(blocks)):
        #     text = blocks[i:i+k]
        #     if len(text)==k:
        #         num = text.count("W")
        #         counts.append(num)
        #     else:
        #         break
        # return(min(counts))
        # if count:  # Check if the list is not empty
        #     return min(count)
        # else:
        #     return -1
        minW = float("inf")
        seen = {"W":0, "B":0}
        left = 0
        for i in range(k):
            seen[blocks[i]] += 1
        
        minW = min(minW, seen["W"])

        for right in range(k, len(blocks)):
            seen[blocks[right]] += 1
            seen[blocks[left]] -= 1
            left += 1
            minW = min(minW, seen["W"])
        
        return minW

        



        