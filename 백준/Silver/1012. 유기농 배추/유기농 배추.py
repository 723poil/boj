class Node:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.link = None

class graph:
    def __init__ (self, x, y):
        self.d = Node(x, y)
    
    def ginsert(self, x, y):
        a = Node(x, y)
        cur = self.d
        while cur.link != None:
            cur = cur.link

        cur.link = a

    def search(self, found, x, y, qocn):
        found[y][x] = 1
        
        w = self.d.link
        while w:
            if found[w.y][w.x] == 0:
                qocn[w.y][w.x].search(found, w.x, w.y, qocn)
            w = w.link
                



# 테스트 케이스 수
T = int(input())

for _ in range(T):

    # 땅읠 가로, 세로 길이, 배추 수
    M,N,K = map(int, input().split())

    # 배추 유무 입력할 배열
    ground = [[0 for _ in range(M)] for _ in range(N)]
    found = [[0 for _ in range(M)] for _ in range(N)]

    # 지렁이 마릿수
    earthworm = 0

    x = []
    y = []

    qocn = [[graph(i,j) for i in range(M)] for j in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
        ground[y[i]][x[i]] = 1
        qocn[y[i]][x[i]] = graph(x,y)

    # 각각의 그래프 생성
    for i in range(K):
        a = qocn[y[i]][x[i]]
        for j in range(4):
            if j == 0:
                if y[i] == 0 :
                    continue
                elif ground[y[i]-1][x[i]] != 0:
                    a.ginsert(x[i], y[i]-1)
            elif j == 1:
                if x[i]+1 == M:
                    continue
                elif ground[y[i]][x[i]+1] != 0:
                    a.ginsert(x[i]+1, y[i])
            elif j == 2:
                if y[i]+1 == N:
                    continue
                elif ground[y[i]+1][x[i]] != 0:
                    a.ginsert(x[i], y[i]+1)
            else:
                if x[i] == 0:
                    continue
                elif ground[y[i]][x[i]-1] != 0:
                    a.ginsert(x[i]-1, y[i])

    # 분리된 그래프 개수 구하기
    for i in range(K):
        if found[y[i]][x[i]] == 0:
            qocn[y[i]][x[i]].search(found, x[i], y[i], qocn)
            earthworm += 1

    print(earthworm)
