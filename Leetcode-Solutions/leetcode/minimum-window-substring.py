class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left = 0
        minSub = ""

        rs = 1000000
        ls = 0

        tCount = Counter(t)
        sCount = {}

        for right in range(len(s)):
            if s[right] in tCount:
                sCount[s[right]] = 1 + sCount.get(s[right] , 0)
            # print("S: ", sCount)


            while self.comp(tCount,sCount):
                size = right - left
                if rs - ls > size:
                    ls = left
                    rs = right
                    minSub = s[ls:rs+1]
               # print(s[ls:rs+1])
               # print("S: ", sCount)

                if s[left] in tCount:
                    sCount[s[left]] -= 1
                    if sCount[s[left]] == 0:
                        sCount.pop(s[left])
                left += 1
                #print("S: ", sCount)
        return minSub            


    def comp(self,tcount,scount):

        if len(scount) != len(tcount):
            return False
        for char in tcount:
            if scount[char]<tcount[char]:
                return False


        return True
            
