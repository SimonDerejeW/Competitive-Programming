n , k = list(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0
dp[1] = abs(nums[1] - nums[0])

for i in range(2 , n):
    res = float('inf')
    for j in range(1,k+1):
        if i - j > -1:
            x = dp[i - j] + abs(nums[i] - nums[i - j])
            res = min(res , x)
        else:
            break
    

    dp[i] = res
print(dp[-1])
