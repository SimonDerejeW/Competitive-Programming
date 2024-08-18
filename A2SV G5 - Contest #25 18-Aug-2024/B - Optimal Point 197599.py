# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

from collections import defaultdict


for _ in range(int(input())):
    n , k = list(map(int, input().split()))
    left = False
    right = False
    for i in range(n):
        l,r = list(map(int, input().split()))
        if l == k:
            left = True
        if r == k:
            right = True
    if left and right:
        print("YES")
    else:
        print("NO")
    
