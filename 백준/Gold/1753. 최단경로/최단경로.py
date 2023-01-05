import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

V, E = map(int, input().split())
startV = int(input())

adj = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

def dijkstra(startv):
    distance = [INF] * (V+1)
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
    
    for i in range(1, V+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])

dijkstra(startV)