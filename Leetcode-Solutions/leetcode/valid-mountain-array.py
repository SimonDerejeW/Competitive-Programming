class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = 0
        dec = 0
        i = 0

        while i < len(arr)-1 and arr[i] < arr[i+1]:
            inc += 1
            i += 1

        print(inc)
        while i < len(arr)-1 and arr[i] > arr[i+1]:
            dec += 1
            i += 1
        print(dec)
        if inc == 0 or dec == 0 or (inc + dec + 1) != len(arr):
            return False
        return True

        
        
            
            