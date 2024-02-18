class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = []
        # postfix = []
        # res = []
        # preProd = postProd = 1

        # for i in range(len(nums)):
        #     preProd *= nums[i]
        #     prefix.append(preProd)
        
        # for j in nums[::-1]:
        #     postProd *= j
        #     postfix.append(postProd)
        
        # postfix.reverse()

        # for k in range(len(nums)):
        #     if k == 0:
        #         res.append(1 * postfix[k+1])
        #     elif k == len(nums)-1:
        #         res.append(1 * prefix[k-1])
            
        #     else:
        #         res.append(prefix[k-1] * postfix[k+1])
        
        # return res

        pref = [1]
        suff = []
        res = []

        prefProd = suffProd = 1

        for i in nums:
            prefProd *= i
            pref.append(prefProd)
        
        for i in nums[::-1]:
            suffProd *= i
            suff.append(suffProd)
        
        suff.reverse()
        suff.append(1)

        for i in range(len(nums)):
            res.append((pref[i]) * (suff[i+1]))
        
        return res







            
