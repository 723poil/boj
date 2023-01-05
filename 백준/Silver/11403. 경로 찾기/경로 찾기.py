import sys

input = sys.stdin.readline

N = int(input())

route = []

for _ in range(N):
    route.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if route[i][k] + route[k][j] > route[i][j] and route[i][k] != 0 and route[k][j] != 0:
                route[i][j] = route[i][k] + route[k][j]

for i in range(N):
    for j in range(N):
        if route[i][j] == 0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print('', end='\n')