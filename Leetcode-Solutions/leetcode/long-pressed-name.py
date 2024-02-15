class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        r = 0
        count = 0
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l+=1
                r+=1
                
            elif name[l] != typed[r] and r-1>=0 and typed[r-1] == typed[r]:
                r+=1  
            else:
                return False
        # print(count)
        while r < len(typed):
            if r > 0 and name[l-1] == typed[r]:
                r += 1
            else:
                return False
        return l == len(name)