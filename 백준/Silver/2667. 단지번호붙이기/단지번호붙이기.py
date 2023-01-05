import sys

input = sys.stdin.readline

N = int(input())

danji = []

for _ in range(N):
    danji.append(str(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * N for _ in range(N)]
home_count = []

def BFS(starty, startx):
    global visited, home_count, danji, dx, dy, count

    queue = []
    visited[starty][startx] = True

    queue.append([starty, startx])
    count += 1

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            sy = y + dy[i]
            sx = x + dx[i]

            if 0 <= sy < N and 0 <= sx < N and danji[sy][sx] == '1' and visited[sy][sx] == False:
                visited[sy][sx] = True
                count += 1
                queue.append([sy, sx])

for i in range(N):
    for j in range(N):
        if danji[i][j] == '1' and visited[i][j] == False:
            count = 0
            BFS(i, j)
            home_count.append(count)

print(len(home_count))

home_count.sort()

while home_count:
    print(home_count.pop(0))