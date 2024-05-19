n = int(input())
nums = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0
dp[1] = abs(nums[1] - nums[0])

for i in range(2 , n):
    x = dp[i - 2] + abs(nums[i] - nums[i - 2])
    y = dp[i - 1] + abs(nums[i] - nums[i - 1])

    dp[i] = min(x , y)
print(dp[-1])
