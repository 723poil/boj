import sys

input = sys.stdin.readline

N = int(input())

vers = [[] for _ in range(N+1)]

for i in range(N):
    a = input().split(' ')

    for j in range(1, len(a), 2):
        if int(a[j]) == -1:
            break
        vers[int(a[0])].append([int(a[j]), int(a[j+1])])

distance = [-1] * (N+1)
distance[1] = 0

def DFS(v, distance):
    for nextv, dis in vers[v]:
        if distance[nextv] == -1:
            distance[nextv] = distance[v] + dis
            DFS(nextv, distance)

DFS(1, distance)

temp = 0
index = 0
for i in range(1,N+1):
    if temp < distance[i]:
        temp = distance[i]
        index = i

distance_last = [-1] * (N+1)
distance_last[index] = 0
DFS(index, distance_last)
print(max(distance_last))