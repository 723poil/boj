T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [[0]*n for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if i==0:
                apart[i][j] = j+1
            else:
                for a in range(j+1):
                    apart[i][j] += apart[i-1][a]
    
    print(apart[k][n-1])