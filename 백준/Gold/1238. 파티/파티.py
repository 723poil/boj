import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

N, M, X = map(int, input().split())

adj = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    istrue = False
    for bx, bc in adj[a]:
        if b == bx and c < bc:
            adj[a].remove([bx, bc])
        elif b == bx:
            istrue = True

    if istrue:
        continue
    adj[a].append([b, c])

def dijkstra(startv, end):
    distance = [INF] * (N+1)
    queue = []
    heapq.heappush(queue, (0, startv))
    distance[startv] = 0

    while queue:
        dis, ver = heapq.heappop(queue)

        for verx, disx in adj[ver]:
            new_dis = dis + disx
            if new_dis < distance[verx]:
                distance[verx] = new_dis
                heapq.heappush(queue, (new_dis, verx))
    if distance[end] == INF:
        return -1

    return distance[end]

m = 0
for i in range(N+1):
    if i == X:
        continue
    m = max(m, dijkstra(i,X)+dijkstra(X, i))

print(m)