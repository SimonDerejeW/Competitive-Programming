class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # lis = []
        # for i in range(len(nums1)):


        # store = {}
        # m_stack = []
        # i = 0
        # while i < len(nums2):
        #     if not m_stack:
        #         m_stack.append(nums2[i])
        #         i += 1
        #     else:
        #         while m_stack and m_stack[-1] < nums2[i]:
        #             store[m_stack.pop()] = nums2[i]
        #         if not m_stack:
        #             m_stack.append(nums2[i])
        #             i += 1
        #         else:
        #             m_stack.append(nums2[i])
        #             i +=
        # for i in range(len(nums1)):
        #     nums1[i] = store.get(nums1[i],-1)
        # return nums1

        dic = {}
        stack = []
        ans = []
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack[-1]] = num
                stack.pop()

            stack.append(num)

        # print(dic)
        for i in nums1:
            if i in dic:
                ans.append(dic[i])
            else:
                ans.append(-1)
        
        return ans
                
                


                
                
