import sys

INF = int(1e9)
input = sys.stdin.readline

TC = int(input())

def bellman_ford(startv, n, ad, dist):
    dist[startv] = 0

    for i in range(1, n+1):
        for fr in range(1, n+1):
            for ver, dis in ad[fr]:
                if dist[ver] > dist[fr] + dis:
                    dist[ver] = dist[fr] + dis
                    if i == n:
                        return 0
    return -1

for _ in range(TC):
    N, M, W = map(int, input().split())

    adj = [[] for _ in range(N+1)]

    for i in range(M):
        a, b, t = map(int, input().split())

        adj[a].append([b, t])
        adj[b].append([a, t])
    
    for i in range(W):
        a, b, t = map(int, input().split())

        adj[a].append([b, -t])
    
    distance = [INF] * (N+1)

    a = bellman_ford(1, N, adj, distance)

    if a == 0:
        print('YES')
    else:
        print('NO')