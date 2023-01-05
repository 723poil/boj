N = int(input())

sort = []

for _ in range(N):
    a, b = map(int, input().split())
    sort.append((a, b))

sort.sort(key=lambda user: (user[1], user[0]))

for i in sort:
    print(i[0], i[1])