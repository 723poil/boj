import sys
input = sys.stdin.readline

N,M = map(int, input().split()) # 1 <= N,M <= 100000

hash = dict()

for i in range(1, N+1):
    b = str(input().rstrip())

    hash[b] = str(i)
    hash[str(i)] = b


for i in range(M):
    b = input().rstrip()
    
    print(hash[b])