import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
    
M, K = map(int, input().split())

B = list(zip( *[list(map(int, input().split())) for _ in range(M)]))

# for i in range(M):
#     B.append(list(map(int, input().split())))

def get_sum(a:list, b:list):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    
    return sum

result = [[0 for _ in range(K)] for _ in range(N)]
    
for i in range(N):
    for j in range(K):
        result[i][j] = str(get_sum(A[i], B[j]))
        
for i in range(N):
    print(" ".join(result[i]))