M, N = map(int, input().split())

chk = [0] * (N+1)

for i in range(2, N+1):
    if chk[i] == 0:
        for j in range(i, N+1, i):
            chk[j] = 1
        chk[i] = 2

for i in range(M, N+1):
    if chk[i] == 2:
        print(i)