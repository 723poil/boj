import sys
import heapq
sys.setrecursionlimit(10**6)
INF = int(1e9)

input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b, c = map(int, input().split())

    adj[a].append([b, c])
    adj[b].append([a, c])

def dijkstra():
    distance = [INF] * (N+1)
    distance[1] = 0
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        dis, ver = heapq.heappop(queue)
        for verx, disx in adj[ver]:
            new_dis = disx + dis
            if new_dis < distance[verx]:
                distance[verx] = new_dis
                heapq.heappush(queue, (new_dis, verx))

    index = 0
    maxd = 0
    for i in range(2, N+1):
        if distance[i] > maxd:
            maxd = distance[i]
            index = i

    return index

dp = 0

def DFS(nown, befn, cost):
    global dp

    if len(adj[nown]) == 1 and cost != 0:
        if dp > cost:
            return
        dp = cost
        return

    for node, dis in adj[nown]:
        if node == befn:
            continue
        DFS(node, nown, dis+cost)

a = dijkstra()

DFS(a, -1, 0)

print(dp)