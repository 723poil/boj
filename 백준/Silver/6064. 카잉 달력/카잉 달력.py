import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    while(x <= M*N):
        if x % N == y % N:
            print(x)
            break
        x += M
    if x > M*N:
        print(-1)