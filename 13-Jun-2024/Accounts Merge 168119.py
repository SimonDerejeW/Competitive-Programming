# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        rank = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                parents[accounts[i][j]] = accounts[i][j]
                rank[accounts[i][j]] = 0
        # print(parents)
        def find(i):
            if parents[i]==i:
                return i
            parents[i] = find(parents[i])
            return parents[i]
             
        def union(x, y):
            x = find(x)
            y = find(y)

            # if x != y:
            if rank[x] > rank[y]:
                parents[y] = x
            elif rank[x] < rank[y]:
                parents[x] = y
            else:
                parents[x] = y
                rank[y] += 1
        
        for i in range(len(accounts)):
            for j in range(1 , len(accounts[i])):
                union(accounts[i][1] , accounts[i][j])
                # print(accounts[i][1] , accounts[i][j])

        minHeap = defaultdict(list)
        # print('par: ',parents)
        # print("smith: ", find('johnsmith@mail.com'))
        for key , val in parents.items():
            x = find(val)
            heappush(minHeap[x] , key)
            # print(minHeap)

        def namer(email):
            for i in range(len(accounts)):
                if email in accounts[i]:
                    return accounts[i][0]

        # print(minHeap)
        res = []
        
        for key in minHeap:
            
            par = namer(key)
            ans = [par]
            while minHeap[key]:
                ans.append(heappop(minHeap[key]))
            res.append(ans)
        return res




