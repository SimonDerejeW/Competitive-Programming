class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string+=str(i)

        num = int(string)
        num+=1
        lis = list(str(num))
        intlis = map(int, lis)
        return list(intlis)

