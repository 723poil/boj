import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N, E = map(int, input().split())

adj = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

must_pass = list(map(int, input().split()))

def dijkstra(startv, endv):
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
    
    return distance[endv]

dis = dijkstra(must_pass[1], must_pass[0])

dis1 = dijkstra(1, must_pass[0]) + dijkstra(must_pass[1], N)
dis2 = dijkstra(1, must_pass[1]) + dijkstra(must_pass[0], N)

mindis = min(dis1, dis2) + dis

if mindis >= INF:
    print(-1)
else:
    print(mindis)