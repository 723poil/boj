import sys
INF = (1e15)

input = sys.stdin.readline

n,m = map(int, input().split())

dp = [[0 for _ in range(101)] for _ in range(101)]
dp2 = [[0 for _ in range(101)] for _ in range(101)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(0, i+1):
        if j-1 >= 0:
            dp[i][j] = dp[i-1][j-1]
            dp2[i][j] = dp2[i-1][j-1]

        dp[i][j] += dp[i-1][j]
        dp2[i][j] += dp2[i-1][j]
        if dp[i][j] >= INF:
            dp2[i][j] += dp[i][j] // INF
            dp[i][j] %= INF

if dp2[n][m] != 0:
    print(int(dp2[n][m]), end='')
    print(int(dp[n][m]))
else:
    print(int(dp[n][m]))