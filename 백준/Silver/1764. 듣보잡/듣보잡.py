from collections import deque
import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    unknown = list()
    both = list()

    for i in range(N+M):
        unknown.append(sys.stdin.readline())
    unknown.sort()

    a = 0
    while a < N+M-1:
        if unknown[a] == unknown[a+1]:
            both.append(unknown[a])
            a += 2
        else:
            a += 1

    print(len(both))
    for i in range(len(both)):
        print(both[i], end='')
