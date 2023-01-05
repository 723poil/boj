import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class linkedlist():
    def __init__(self, ver, true):
        self.ver = ver
        self.istrue = true
        self.link = None
        self.trueparty = []

    def linsert(self, ver, true):
        cur = self
        while cur.link:
            cur = cur.link

        cur.link = linkedlist(ver,true)

def research(v):
    global party, llmember

    a = llmember[v]

    while a:
        for i in llmember[a.ver].trueparty:
            if party[i] == False:
                party[i] = True
        a = a.link

def bfs(v):
    global N,M, party, llmember, visited

    queue = deque()
    queue.append(llmember[v])

    while queue:
        w = queue.popleft()

        while w:
            if w.istrue == True and visited[w.ver] == False:
                visited[w.ver] = True

                for i in llmember[w.ver].trueparty:
                    party[i] = True
                
                a = llmember[w.ver]
                while a:
                    if llmember[a.ver].istrue == False:
                        research(a.ver)
                        llmember[a.ver].istrue = True
                        if visited[a.ver] == True:
                            visited[a.ver] = False

                    a = a.link

            elif visited[w.ver] == False:
                visited[w.ver] = True
                for i in llmember[w.ver].trueparty:
                    if party[i] == True:
                        llmember[w.ver].istrue = True
                        for j in llmember[w.ver].trueparty:
                            party[j] = True
                        visited[w.ver] = False
                        break
                queue.append(llmember[w.ver])
                
            w = w.link

N, M = map(int, input().split())

party = [False for _ in range(M+1)] # 파티의 수에 맞게 구성

trueknow = list(map(int, input().split())) # 진실을 알고 있는 사람 리스트

llmember = [linkedlist(i, False) for i in range(N+1)] # 구성원 구성

for i in range(1, trueknow[0]+1):
    llmember[trueknow[i]].istrue = True # 진실을 알고 있는 멤버 업데이트

for i in range(1, M+1):             # 파티 구성원들 서로 연결
    linkmember = list(map(int, input().split()))
    
    for j in range(1, linkmember[0]+1):
        for k in range(1, linkmember[0]+1):
            if j == k:
                continue
            llmember[linkmember[j]].linsert(linkmember[k], llmember[linkmember[k]].istrue)
    
    for j in range(1, linkmember[0]+1): # 각 구성원들이 속한 파티 업데이트
        llmember[linkmember[j]].trueparty.append(i)

visited = [False for _ in range(N+1)]

for i in range(1, N+1):
    if visited[i] == False:
        bfs(i)

count = 0

for i in range(1, M+1):
    if party[i] == False:
        count += 1

print(count)