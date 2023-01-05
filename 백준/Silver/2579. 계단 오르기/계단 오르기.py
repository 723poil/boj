import sys
sys.setrecursionlimit(10**6)

N = int(input())

stairs = [0] * 301

for i in range(N):
    stairs[i+1] = int(input())

dp = [0] * 301

dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(3, N):
    dp[i+1] = max(dp[i-2] + stairs[i] + stairs[i+1], dp[i-1] + stairs[i+1])

print(dp[N])