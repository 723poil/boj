def search(a, b, board):
    sum = 0
    check = board[a][b]
    for i in range(a, a+8):
        for j in range(b, b+8, 2):
            if board[i][j] == check:
                sum += 1
            if board[i][j+1] != check:
                sum += 1
        if check == 'B':
            check = 'W'
        else:
            check = 'B'

    return sum  

M, N = map(int, input().split())

chessboard = []
for i in range(M):
    a = str(input())
    chessboard.append(a)

binaryboard = [[0]*N for _ in range(M)]
sum = []

for i in range (0, M-7):
    for j in range(0, N-7):
        sum.append(search(i, j, chessboard))

print(min(min(sum), 64-max(sum)))