n = int(input())

# 1 - 1
# 2 - 3
# 3 - 5
# 4 - 11
# 5 - 21
# 6 - 43
# 7 - 85
# 8 - 171
# dp[i] = dp[i-1] + dp[i-2] * 2

dp = [0, 1, 3]

for i in range(3, n+1):
    dp.append((dp[i-1] + dp[i-2] * 2) % 10007)

print(dp[n] )