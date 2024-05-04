# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from collections import defaultdict

n , m , k =list(map(int, input().split()))

parents = {i:i for i in range(1,n+1)}
rank = defaultdict(int)

def find(x):
    if x == parents[x]:
        return x
    par = find(parents[x])
    parents[x] = par
    return par

def union(x, y):
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
def is_connected(x , y):
    return find(x) == find(y)

for i in range(m):
    input()
queries = []
for i in range(k):
    queries.append(list(input().split()))

res = []
for i in range(len(queries) - 1, -1, -1):
    op , x , y = queries[i]
    if op == 'ask':
        ans = is_connected(int(x) , int(y))
        res.append(ans)
    else:
        union(int(x) , int(y))

for i in range(len(res) - 1 , -1 , -1):
    if res[i]:
        print("YES")
    else:
        print("NO")

        
