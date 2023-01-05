import sys

input = sys.stdin.readline

N,M = map(int, input().split())

miro = []

for _ in range(N):
    miro.append(str(input()))

visited = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(starty, startx):
    global dx, dy, miro, visited

    queue = []
    visited[starty][startx] = True

    queue.append([starty, startx, 1])

    while queue:
        y, x, count = queue.pop(0)

        for i in range(4):
            sy = y + dy[i]
            sx = x + dx[i]

            if 0 <= sy < N and 0 <= sx < M and miro[sy][sx] == '1' and visited[sy][sx] == False:
                if sy == N-1 and sx == M-1:
                    print(count+1)
                    return
                
                visited[sy][sx] = True
                queue.append([sy,sx, count+1])

BFS(0,0)