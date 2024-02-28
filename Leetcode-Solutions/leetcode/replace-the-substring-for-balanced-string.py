class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        need = {"Q": 0 , "W": 0 , "R": 0, "E": 0}
        seen = {"Q": 0 , "W": 0 , "R": 0, "E": 0}
        left = 0
        minLen = float("inf")

        for key in counter:
            if counter[key] > (len(s) // 4):
                need[key] = counter[key] - (len(s) // 4)
        
        if sum(need.values()) == 0:
            return 0
        # print(need)
        for right in range(len(s)):
            seen[s[right]] += 1
            while seen["Q"] >= need["Q"] and seen["W"] >= need["W"] and seen["E"] >= need["E"] and seen["R"] >= need["R"]:
                minLen = min(minLen , (right - left + 1))
                seen[s[left]] -= 1
                left += 1
        
        return minLen


        