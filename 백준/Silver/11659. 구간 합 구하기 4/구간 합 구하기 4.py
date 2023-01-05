import sys

input = sys.stdin.readline

N,M = map(int, input().split())

number = list(map(int, input().split()))
ssum = [0, number[0]]

for i in range(1, N):
    ssum.append(ssum[-1] + number[i])

for _ in range(M):
    i, j = map(int , input().split())

    print(ssum[j] - ssum[i-1])