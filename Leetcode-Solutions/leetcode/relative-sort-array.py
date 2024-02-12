class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # dic = {}
        # for idx, value in enumerate(arr2):
        #     dic[value] = idx
        # # def checker(x):
        # #     dic[x]
            

        # relative_sort = sorted(arr1, key=lambda x: dic[x])
        # return relative_sort


        n = len(arr1)
        m = len(arr2)

        def compare(item):
            if item not in arr2:
                return m + 1
            return arr2.index(item)

        arr1.sort()
        arr1.sort(key=compare)
        

        return arr1

        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]




        