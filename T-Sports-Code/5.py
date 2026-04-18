n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[float("inf")] * m for _ in range(n)]
dp[0][0] = 0



for r in range(n-1):
    for c in range(m-1):
        dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
