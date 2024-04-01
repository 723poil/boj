from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**5)
input = stdin.readline

M, N = map(int, input().split())
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
maps = []
dp = []

def dfs(cur: tuple):
    global M, N, x, y, maps, dp
    if cur[0] == M-1 and cur[1] == N-1:
        return 1
    
    if dp[cur[0]][cur[1]] != -1:
        return dp[cur[0]][cur[1]]
    
    count = 0
    for i in range(4):
        rcur = (cur[0] + y[i], cur[1] + x[i])
        
        # 범위 밖 인덱스 체크
        if not (0 <= rcur[0] < M and 0 <= rcur[1] < N):
            continue

        # 내리막길 체크
        if maps[cur[0]][cur[1]] <= maps[rcur[0]][rcur[1]]:
            continue
        
        count += dfs(rcur)
    
    dp[cur[0]][cur[1]] = count
    return count

def solution():
    global maps, M, N, dp
    
    for _ in range(M):
        maps.append(list(map(int, input().split())))
        dp.append([-1 for _ in range(N)])
        
    return dfs((0, 0))

print(solution())