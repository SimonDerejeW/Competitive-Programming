class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0}
        for bill in bills:
            if bill == 5 : 
                change[5] +=1

            elif bill == 10 and change[5]: 
                change[10] +=1
                change[5] -= 1

            elif bill == 20 and ((change[5] and change[10]) or change[5] >=3):
                if change[5] and change[10]:
                    change[5] -= 1
                    change[10] -=1
                else: 
                    change[5] -=3
            else : return False
            
        return True
                