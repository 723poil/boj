N, M = map(int, input().split())

minn = 9999999999
idx = N+1
cb = [[9999999999 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    
    cb[a][b] = 1
    cb[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1, N+1):
            if cb[i][k] + cb[k][j] < cb[i][j]:
                cb[i][j] = cb[i][k] + cb[k][j]

for i in range(N, 0, -1):
    sum = 0
    for j in range(1, N+1):
        if i != j:
            sum += cb[i][j]

    if minn >= sum:
        if minn == sum:
            idx = min(idx, i)
        else:
            idx = i
            minn = sum

print(idx)