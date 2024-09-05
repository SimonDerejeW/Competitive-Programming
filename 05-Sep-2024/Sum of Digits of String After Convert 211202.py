# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = []
        for char in s:
            convert.append(str(ord(char) - 96))
        convert = "".join(convert)
        # print(convert)
        score = convert
        for i in range(k):
            x = 0
            for char in score:
                x += int(char)
            score = str(x)
        return int(score)


