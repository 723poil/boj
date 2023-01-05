import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int, input().split())

tomato = []
goodtomato = deque()
totalcount = 0

for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            goodtomato.append([i, j, 0])
        elif tomato[i][j] == -1:
            totalcount += 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():
    global goodtomato, tomato, totalcount
    lastcount = 0
    while goodtomato:
        y, x, count = goodtomato.popleft()
        totalcount += 1
        lastcount = count
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    goodtomato.append([ny, nx, count + 1])

    if totalcount != M*N:
        print(-1)
        return
    
    print(lastcount)
    return

BFS()