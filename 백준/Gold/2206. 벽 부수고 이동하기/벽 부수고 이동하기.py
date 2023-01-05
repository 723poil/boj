import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maap = [[] for _ in range(N+1)]

for i in range(1,N+1):
    maap[i] = (list(str(input())))
    maap[i].insert(0, 0)

def BFS():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    visited = [[False for _ in range(M+1)] for _ in range(N+1)]
    breakvisited = [[False for _ in range(M+1)] for _ in range(N+1)]
    visited[1][1] = True
    queue = deque()
    queue.append([1, 1, 1, False])
    while queue:
        y, x, cost, isbreak = queue.popleft()

        if y == N and x == M:
            print(cost)
            return

        for i in range(4):
            sy = y + dy[i]
            sx = x + dx[i]

            if 0<sy<=N and 0<sx<=M and visited[sy][sx] == False:
                if isbreak:
                    if int(maap[sy][sx]) == 0 and breakvisited[sy][sx] == False:
                        breakvisited[sy][sx] = True
                        queue.append([sy,sx,cost+1, isbreak])
                else:
                    if int(maap[sy][sx]) == 0:
                        visited[sy][sx] = True
                        queue.append([sy, sx, cost+1, isbreak])
                    else:
                        visited[sy][sx] = True
                        queue.append([sy, sx, cost+1, True])

    
    print(-1)
    return

BFS()