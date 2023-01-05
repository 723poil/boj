import sys

n = int(input())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))
