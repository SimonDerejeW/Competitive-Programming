# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self , n):
        self.parents = {i:i for i in range(1,n+1)}
        self.rank = defaultdict(int)
        self.count = 0

    def find(self,x):
        # Write your code here
        if x == self.parents[x]:
            return x
        par = self.find(self.parents[x])
        self.parents[x] = par
        return par
    
    def union(self,x, y):
    # Write your code here
        x = self.find(x)
        y = self.find(y)

        if x == y:
            self.count += 1
            return True

        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parents[y] = x
            elif self.rank[x] < self.rank[y]:
                self.parents[x] = y
            else:
                self.parents[x] = y
                self.rank[y] += 1
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_al = UnionFind(n)
        uf_bob = UnionFind(n)

        edges.sort(key = lambda x : x[0], reverse = True)
        
        for op , u , v in edges:
            if op == 1:
                uf_al.union(u , v)
            elif op == 2:
                uf_bob.union(u , v)
            else: 
                a = uf_al.union(u , v)          
                b = uf_bob.union(u , v)
                if a and b:
                    uf_al.count -= 1


        og = uf_al.find(1)
        og1 = uf_bob.find(1)
        flag = True
        flagg = True
        for i in range(1 , n+1):
            if uf_al.find(i) != og:
                flag = False
                break
        for i in range(1 , n+1):
            if uf_bob.find(i) != og1:
                flagg = False
                break
        
        if flag and flagg:
            return uf_al.count + uf_bob.count
        return -1
        
               
























