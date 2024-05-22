n = int(input())
grid = []
for _ in range(n):
    nums = list(map(int, input().split()))
    grid.append(nums)

for i in range(len(grid) - 2 , -1 , -1):
    for j in range(3):
        if j == 0:
            grid[i][j] += max(grid[i + 1][1] , grid[i + 1][2])
        elif j == 1:
            grid[i][j] += max(grid[i + 1][0] , grid[i + 1][2])
        else:
            grid[i][j] += max(grid[i + 1][0] , grid[i + 1][1])
print(max(grid[0]))
