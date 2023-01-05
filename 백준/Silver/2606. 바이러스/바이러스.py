import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.ver = data
        self.link = None

class graph:
    def __init__(self, data):
        self.pointer = Node(data)

    def qinsert(self, data):
        cur = self.pointer

        while cur.link:
            cur = cur.link
        cur.link = Node(data)

    def qpop(self):
        temp = self.pointer
        self.pointer = temp.link
        return temp.ver

N= int(input())
M= int(input())

computer = [graph(i) for i in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())

    computer[a].qinsert(b)
    computer[b].qinsert(a)

for i in range(N+1):
    computer[i].qpop()

count = 0
found = [0]*(N+1)
def DFS(start):
    global count, computer, found
    found[start] = 1
    w = computer[start].pointer

    while w:
        if found[w.ver] == 0:
            found[w.ver] = 1
            count += 1
            DFS(w.ver)
        w = w.link

DFS(1)

print(count)