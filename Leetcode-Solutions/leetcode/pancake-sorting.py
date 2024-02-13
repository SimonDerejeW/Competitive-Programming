class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # k = []
        # z=0
        # for i in range(len(arr)-1):
        #     big_idx = arr.index(max(arr))
        #     k.append(big_idx)
        #     arr = arr[big_idx::-1] + arr[big_idx+1:]
        #     arr = arr[::-1]
        #     k.append(len(arr)-i)
        #     arr = arr[:len(arr)-1-i]
        # return k
        size = len(arr)
        nums = arr.copy()
        nums.sort()
        k = 0
        res = []
        while k < size:
            currMax = arr.index(max(arr[:size-k]))
            arr[:currMax+1] = reversed(arr[:currMax+1])
            
            arr[:size-k] = reversed(arr[:size-k])
            res.append(currMax + 1)
            res.append(size-k)
            k+=1
        return res
        