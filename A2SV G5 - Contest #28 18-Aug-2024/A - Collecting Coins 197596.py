# Problem: A - Collecting Coins - https://codeforces.com/gym/540354/problem/A


for _ in range(int(input())):
    a , b ,c , n = list(map(int, input().split()))
    diff = (max(a,b,c) - a) + (max(a,b,c) - b) + (max(a,b,c) - c)
    diff = n - diff
    ans = diff >= 0 and diff % 3 == 0
    if ans:
        print("YES")
    else:
        print("NO")
    