s = input()
t = input()
n , m = len(s) , len(t)

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = 1 + dp[i][j]
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1] , dp[i + 1][j])

i = n
j = m
res = []

while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        res.append(s[i - 1])
        i -= 1
        j -= 1
    elif dp[i][j - 1] > dp[i - 1][j]:
        j -= 1
    else:
        i -= 1

print("".join(res[::-1]))
