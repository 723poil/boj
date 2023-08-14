import sys

input = sys.stdin.readline

N = int(input())

T = [0]*(N+1)
P = [0]*(N+1)

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

maxSum = 0

def dfs(idx, cur_sum):
    global T, P, N, maxSum
    
    if idx + T[idx] - 1 < N+1:
        cur_sum += P[idx]
        next_day = idx + T[idx]
        
        if next_day <= N:
            for i in range(next_day, N+1):
                dfs(i, cur_sum)
        else:
            maxSum= max(maxSum, cur_sum)
            return
    else:
        maxSum = max(maxSum, cur_sum)
        return
        
for i in range(1, N+1):
    dfs(i, 0)
    
print(maxSum)