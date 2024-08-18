# Problem: B - Fasika and Children - https://codeforces.com/gym/538762/problem/B

from collections import deque


n , m = list(map(int, input().split()))
nums = list(map(int, input().split()))

que = deque()

for i in range(len(nums)):
    que.append([nums[i] , i+1])

last = n
while que:
    x, idx = que.popleft()
    x-=m
    if x > 0:
        last = idx
        que.append([x,idx])
print(last)
