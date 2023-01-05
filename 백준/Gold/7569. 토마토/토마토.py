from collections import deque
import sys

input = sys.stdin.readline

M,N,H = map(int, input().split())

tomato = [[] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, input().split())))

visited = [[[False] * M for _ in range(N)] for _ in range(H)]
queue = deque()

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i,j,k,0])

lastcount = 0

def BFS():
    global queue, visited, tomato, M,N,H, dx, dy, dz, lastcount

    while queue:
        z, y, x, count = queue.popleft()
        lastcount = count

        for i in range(6):
            sz = z + dz[i]
            sy = y + dy[i]
            sx = x + dx[i]

            if 0<=sz<H and 0<=sy<N and 0<=sx<M and visited[sz][sy][sx] == False and tomato[sz][sy][sx] == 0:
                visited[sz][sy][sx] = True
                tomato[sz][sy][sx] = 1
                queue.append([sz,sy,sx,count+1])
                

BFS()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:
                print(-1)
                break
            elif z==H-1 and y==N-1 and x==M-1:
                print(lastcount)
        if tomato[z][y][x] == 0:
            break
    if tomato[z][y][x] == 0:
        break