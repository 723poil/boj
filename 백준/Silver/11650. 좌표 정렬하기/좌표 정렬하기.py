N = int(input())

coord = []

for i in range(N):
    a, b = map(int, input().split())

    coord.append((a, b))

coord.sort(key=lambda user:(user[0], user[1]))



for i in coord:
    print(i[0], i[1])