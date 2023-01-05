import sys

input = sys.stdin.readline

class Node:
    def __init__(self, ver):
        self.ver = ver
        self.link = None

class graph:
    def __init__(self, ver):
        self.pointer = Node(ver)

    def glink(self, ver):
        cur = self.pointer
        temp = Node(ver)

        temp.link = cur.link

        cur.link = temp

    def gdelete(self):
        temp = self.pointer

        self.pointer = temp.link

        return temp.ver

def DFS(startv):
    global visited, vertex
    visited[startv] = True

    w = vertex[startv].pointer
    while w:
        if visited[w.ver] == False:
            visited[w.ver] = True
            DFS(w.ver)

        w = w.link


N, M = map(int, input().split())

vertex = [graph(-1) for _ in range(N+1)]

for i in range(M):
    ver1, ver2 = map(int, input().split())

    vertex[ver1].glink(ver2)
    vertex[ver2].glink(ver1)

for i in range(1, N+1):
    vertex[i].gdelete()

visited = [False for _ in range(N+1)]

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        DFS(i)
        count += 1

print(count)