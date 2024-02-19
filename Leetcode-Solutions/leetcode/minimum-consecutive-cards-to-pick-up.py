class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minLength = float("inf")
        seen = defaultdict(int)
        left = 0

        for right in range(len(cards)):
            seen[cards[right]] += 1
            # size = right - left + 1
            while len(seen) < right - left + 1:
                minLength = min(minLength, right - left + 1)
                seen[cards[left]] -= 1
                if seen[cards[left]] == 0:
                    seen.pop(cards[left])
                left += 1
            
        if minLength == float("inf"):
            return -1
        else:
            return minLength