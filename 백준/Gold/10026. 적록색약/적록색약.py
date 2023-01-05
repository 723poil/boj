import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

dis = []
visited = []

lstcount = 0
lstcwncount = 0

for i in range(N):
    dis.append(str(input()))
    visited.append([False for _ in range(len(dis[i]))])

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

def DFS(y, x, q):
    global dis, visited, dx, dy

    visited[y][x] = True

    for i in range(4):
        sy = y + dy[i]
        sx = x + dx[i]

        if 0<=sy<N and 0<=sx<len(dis[sy])-1 and visited[sy][sx] == False and dis[sy][sx] == dis[y][x]:
            DFS(sy,sx, q)
        elif 0<=sy<N and 0<=sx<len(dis[sy])-1 and visited[sy][sx] == False and dis[sy][sx] != dis[y][x]:
            q.append([sy, sx])

def cwnDFS(y, x, q):
    global dis, visited, dx, dy

    visited[y][x] = False

    for i in range(4):
        sy = y + dy[i]
        sx = x + dx[i]

        if 0<=sy<N and 0<=sx<len(dis[sy])-1 and visited[sy][sx] == True and dis[sy][sx] == dis[y][x]:
            cwnDFS(sy,sx, q)
        elif 0<=sy<N and 0<=sx<len(dis[sy])-1 and visited[sy][sx] == True and dis[sy][sx] != dis[y][x]:
            if dis[sy][sx] == 'B':
                q.append([sy, sx])
            elif dis[y][x] == 'B':
                q.append([sy, sx])
            else:
                cwnDFS(sy,sx, q)


def BFS():
    global dis, visited, lstcount, lstcwncount

    queue = deque()
    queue.append([0, 0])

    while queue:
        y, x = queue.popleft()

        if visited[y][x] == False:
            lstcount += 1
            DFS(y, x, queue)

    queue.append([0, 0])    
    
    while queue:
        cy, cx = queue.popleft()

        if visited[cy][cx] == True:
            lstcwncount += 1
            cwnDFS(cy, cx, queue)

BFS()

print(lstcount, lstcwncount)