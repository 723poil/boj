import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for i in range(M):
    a, b, dis = map(int, input().split())

    adj[a].append([b, dis])

startV, endV = map(int, input().split())

def dijkstra(startv, endv):
    distance = [INF] * (N+1)
    distance[startv] = 0
    queue = []

    heapq.heappush(queue, [0, startv])

    while queue:
        dis, ver = heapq.heappop(queue)

        if distance[ver] < dis:
            continue

        for verx, disx in adj[ver]:
            new_dis = dis + disx

            if distance[verx] > new_dis:
                distance[verx] = new_dis
                heapq.heappush(queue, [new_dis, verx])
    
    print(distance[endv])

dijkstra(startV, endV)