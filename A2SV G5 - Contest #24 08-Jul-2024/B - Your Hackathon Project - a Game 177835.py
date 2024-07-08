# Problem: B - Your Hackathon Project - a Game - https://codeforces.com/gym/534160/problem/B

n , m = list(map(int, input().split()))
height = list(map(int, input().split()))
query = []
for _ in range(m):
    x = list(map(int, input().split()))
    query.append(x)

pref = [0]
suff = [0]

curr = height[0]
diff = 0

for i in range(1,len(height)):
    if height[i] < curr:
        diff += abs(curr-height[i])
    pref.append(diff)
    curr = height[i]

curr = height[-1]
diff = 0

for j in range(len(height)-2, -1,-1):
    if height[j] < curr:
        diff += abs(curr-height[j])
    suff.append(diff)
    curr=height[j]
# print(pref)
suff = suff[::-1]
for x , y in query:
    if x < y:
        print(pref[y-1] - pref[x-1])
    else:
        print(abs(suff[x-1] - suff[y-1]))




