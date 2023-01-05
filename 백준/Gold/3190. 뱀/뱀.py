import sys
from collections import deque
from typing import Any

if __name__ == '__main__':
    N = int(sys.stdin.readline()) # 보드의 크기 N X N

    board = [[-1 for i in range(N+2)] for i in range(N+2)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            board[i][j] = 0 

    K = int(sys.stdin.readline()) # 사과의 개수
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[x][y] = 1

    L = int(sys.stdin.readline())

    direction_change = deque()
    for i in range(L):
        X, C = map(str, sys.stdin.readline().split(' '))
        direction_change.append(deque([int(X), str(C[0])]))

    time_second = 0
    direction = 1
    snake = deque([[int(1),int(1)]])
    snake_head = deque([int(1),int(1)])

    Game_set = True
    while Game_set:
        

        if direction == 1:
            snake_head[1] += 1
            snake.append([snake_head[0], snake_head[1]])
        elif direction == 0:
            snake_head[0] -= 1
            snake.append([snake_head[0], snake_head[1]])
        elif direction == 2:
            snake_head[0] += 1
            snake.append([snake_head[0], snake_head[1]])
        else:
            snake_head[1] -= 1
            snake.append([snake_head[0], snake_head[1]])

        time_second += 1

        if len(direction_change)>0 and time_second == int(direction_change[0][0]):
            str_direction = str(direction_change[0][1])
            if str_direction == 'L':
                direction -= 1
                if direction < 0:
                    direction = 3
            else :
                direction += 1
                if direction > 3:
                    direction = 0
            direction_change.popleft()

        for i in range(len(snake)):
            if i != len(snake)-1 and snake[i][0] == snake_head[0] and snake[i][1] == snake_head[1] or board[snake_head[0]][snake_head[1]] == -1:
                print(time_second)
                Game_set = False
                break

        if board[snake_head[0]][snake_head[1]] == 1:
            board[snake_head[0]][snake_head[1]] = 0
        else :
            snake.popleft()