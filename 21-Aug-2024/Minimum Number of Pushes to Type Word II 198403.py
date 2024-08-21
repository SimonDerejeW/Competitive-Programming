# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = defaultdict(int)
        for char in word:
            letters[char] += 1
        
        sorted_letters = sorted(letters.items(), key=lambda x:x[1], reverse = True)
        count = 1
        k = 8
        score = 0
        

        for i in range(len(sorted_letters)):
            if k == 0:
                k = 8
                count += 1
            score += ((sorted_letters[i][1]) * count)
            k -= 1
        return score