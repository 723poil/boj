import sys

input = sys.stdin.readline

N, M = map(int, input().split())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

sum = 0

def rectangle_1x4():
    global paper, N, M, sum

    dx = [3, 0]
    dy = [0, 3]

    for i in range(N):
        for j in range(M):
            for k in range(2):
                sy = i + dy[k]
                sx = j + dx[k]

                if 0<= sy < N and 0<= sx < M and k == 0:
                    sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i][j+3])
                elif 0<= sy < N and 0<= sx < M and k == 1:
                    sum = max(sum, paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+3][j])

def rectangle_2x2():
    global paper, N, M, sum

    for i in range(N):
        for j in range(M):
            sy = i + 1
            sx = j + 1

            if 0<= sy < N and 0<= sx < M:
                sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1])

def rectangle_3x2():
    global paper,N, M, sum

    dx = [1, 2, -1, -2, 1, 2, -1, -2]
    dy = [2, -1, -2, 1, -2, 1, 2, -1]

    for i in range(N):
        for j in range(M):
            for k in range(8):
                sx = j + dx[k]
                sy = i + dy[k]

                if k == 0 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j+1])
                elif k == 1 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i-1][j+2])
                elif k == 2 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i-1][j]+paper[i-2][j]+paper[i-2][j-1])
                elif k == 3 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i][j-1]+paper[i][j-2]+paper[i+1][j-2])
                elif k == 4 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i-1][j]+paper[i-2][j]+paper[i-2][j+1])
                elif k == 5 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+2])
                elif k == 6 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j-1])
                elif k == 7 and 0<=sx<M and 0<=sy<N:
                    sum = max(sum, paper[i][j]+paper[i][j-1]+paper[i][j-2]+paper[i-1][j-2])

def rectangle_2x2_2():
    global paper, N, M, sum
    
    dx = [1, 2, 1, 2]
    dy = [2, 1, 2, 1]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                sx = j + dx[k]
                sy = i + dy[k]

                if k == 0 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1])
                elif k == 1 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i+1][j]+paper[i+1][j+1]+paper[i][j+1]+paper[i][j+2])
                elif k == 2 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j])
                elif k == 3 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+1][j+2])

def rectangle_3x1():
    global paper, N, M, sum

    dx = [2, 1, 2, 1]
    dy = [1, 2, 1, 2]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                sx = j + dx[k]
                sy = i + dy[k]

                if k == 0 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i][j+2])
                elif k == 1 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j])
                elif k == 2 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i+1][j]+paper[i+1][j+1]+paper[i][j+1]+paper[i+1][j+2])
                elif k == 3 and 0<=sy<N and 0<=sx<M:
                    sum = max(sum, paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1])


rectangle_1x4()
rectangle_2x2()
rectangle_3x2()
rectangle_2x2_2()
rectangle_3x1()

print(sum)