N = int(input())

info = []

for i in range(N):
    a, b = map(int, input().split())
    info.append([a, b, int(1)])

for i in range(N):
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            info[i][2] += 1

for i in range(N):
    print(info[i][2], end = ' ')