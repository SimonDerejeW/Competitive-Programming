# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parents = {i:i for i in range(n)}
        rank = defaultdict(int)
        summ = defaultdict(int)
        arr = [0] * n
        

        def find(x):
        # Write your code here
            if x == parents[x]:
                return x
            par = find(parents[x])
            parents[x] = par
            return par
        
        def union(x, y):
        # Write your code here
            x = find(x)
            y = find(y)

            if x != y:
                if rank[x] > rank[y]:
                    parents[y] = x
                elif rank[x] < rank[y]:
                    parents[x] = y
                else:
                    parents[x] = y
                    rank[y] += 1
        maxSum = 0
        res = []

        for i in range(len(removeQueries) - 1 , -1 , -1):
            res.append(maxSum)
            idx = removeQueries[i]
            num = nums[idx]
            arr[idx] = num

            if ((idx - 1 < 0) or ((idx - 1 > -1) and arr[idx - 1] == 0)) and ((idx + 1 >= n) or ((idx + 1 < n) and arr[idx + 1] == 0)):
                summ[idx] += num
                # print('1: ',summ)
                # arr[idx] = num
                maxSum = max(maxSum , summ[idx])
            elif ((idx - 1 > -1) and arr[idx - 1] != 0) and ((idx + 1 < n and arr[idx + 1] != 0)):
                # print('in')
                sum_of_left = summ[find(idx - 1)]
                sum_of_right = summ[find(idx + 1)]
                union(idx, idx - 1)
                union(idx , idx + 1)
                x = find(idx)
                # print(sum_of_left , sum_of_right)
                summ[x] = (sum_of_left + sum_of_right) + num
                maxSum = max(maxSum , summ[x])

            elif (idx - 1 > -1) and arr[idx - 1] != 0:
                # print('2: ',summ)
                union(idx , idx - 1)
                x = find(idx)
                summ[x] += num
                maxSum = max(maxSum , summ[x])
            elif (idx + 1 < n and arr[idx + 1] != 0):
                # print('3: ',summ)
                union(idx , idx + 1)
                x = find(idx)
                summ[x] += num
                maxSum = max(maxSum , summ[x])
        res.reverse()
        return res






















        
