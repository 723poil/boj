import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list()

for i in range(N):
    A.append(list(map(int, input().split())))
    
M, K = map(int, input().split())

B = list()

for i in range(M):
    B.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(K):
        sum = 0
        for k in range(M):
            sum += (A[i][k] * B[k][j])
        print(sum, end=" ")
    print()