import sys

input = sys.stdin.readline

N = int(input())



# 1 - 1
# 2 - 10
# 3 - 101 100
# 4 - 1001 1000 1010
# 5 - 10000 10001 10010 10100 10101 
dp = [0] * (N+1)

dp[1] = 1

if N > 1:
    dp[2] = dp[1]

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
        
print(dp[N])