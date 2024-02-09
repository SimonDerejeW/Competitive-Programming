class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # n = len(shifts)
        # k = ""
        # prevSum = [0] * len(s)
        # prefix = []
        # summ = 0
        # for start, end, inc in shifts:
        #     x = -1
        #     if inc == 1:
        #         x = 1
            
        #     prevSum[start] += x
        #     if end + 1 < len(s):
        #         prevSum[end+1] -= x
        
        # for i in prevSum:
        #     summ += i
        #     prefix.append(summ)
        

        # for i in range(len(s)):
        #     char = ord(s[i])+ prefix[i]
        #     while char > 122:
        #         char = char - 122 +96
        #     while char < 97:
        #         char = char - 96 + 122
            
        #     k += chr(char)
        
        # return k

        prev = [0] * len(s)

        for i,j,k in shifts:
            x = -1
            if k == 1:
                x = 1
            
            prev[i] += x

            if j < len(prev)-1:
                prev[j+1] -= x
            
        for i in range(1,len(prev)):
            prev[i] += prev[i-1]
        
        
        res = []
        for i in range(len(prev)):
            character = chr(((ord(s[i]) - ord("a") + prev[i])%26)+97)
            res.append(character)
        return "".join(res)
            
            







        