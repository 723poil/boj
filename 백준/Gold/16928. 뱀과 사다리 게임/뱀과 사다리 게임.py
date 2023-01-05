import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

ladder = []
snake = []

lors = [-1 for _ in range(101)]
visited = [False for _ in range(101)]

for i in range(N):
    ladder.append(list(map(int, input().split())))
    lors[ladder[i][0]] = i

for i in range(M):
    snake.append(list(map(int, input().split())))
    lors[snake[i][0]] = i + N

def BFS():
    global N, M, ladder, snake, lors

    queue = deque()
    queue.append([1, 0])

    while queue:
        x, count = queue.popleft()

        if x == 100:
            print(count)
            return

        for i in range(1, 7):
            if x+i <= 100 and visited[x+i] == False:
                if lors[x+i] != -1 and lors[x+i] < N:
                    queue.append([ladder[lors[x+i]][1], count+1])
                    visited[x+i] = True
                    visited[ladder[lors[x+i]][1]] = True   
                elif lors[x+i] != -1:
                    queue.append([snake[lors[x+i]-N][1], count+1])
                    visited[x+i] = True
                    visited[snake[lors[x+i]-N][1]] = True
                else:
                    queue.append([x+i, count+1])
                    visited[x+i] = True
                

BFS()