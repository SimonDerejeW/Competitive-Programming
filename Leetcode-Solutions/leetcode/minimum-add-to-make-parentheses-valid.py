class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # dic = { "(": 0, ")": 0}
        # for i in s:
        #     dic[i] += 1
        
        # print(dic)
        # return abs(dic["("] - dic[")"])
        valid = []
        for i in s:
            if i == "(":
                valid.append(i)
            else:
                if len(valid) > 0 and valid[-1] == "(":
                    valid.pop()
                else:
                    valid.append(")")
        # print(valid)
        return len(valid)

