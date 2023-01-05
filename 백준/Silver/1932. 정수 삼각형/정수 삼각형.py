import sys

N = int(input())

triangle = [[0] * 501 for i in range(501)]

triangle[1][1] = int(input())

index = 2

for i in range(1,N):
    triangle[i+1][1:index+1] = map(int, sys.stdin.readline().rstrip().split())
    index += 1

dp = [[0] * 501 for i in range(501)]
dp[1][1] = triangle[1][1]

for i in range(2, N+1):
    
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[N]))
