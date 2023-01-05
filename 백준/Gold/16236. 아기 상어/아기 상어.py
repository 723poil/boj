import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

sea = []

for _ in range(N):
    sea.append(list(map(int, input().split())))

fish = deque()
shark = [2,-1,-1] # size, y, x
time = 0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark[1] = i
            shark[2] = j
        elif sea[i][j] != 0:
            fish.append([sea[i][j], i, j]) # size, y, x

cnt = 0

def BFS(y, x): # 좌표 하나를 넣어 상어에서 갈수있는 거리 구하기
                    # 상어보다 큰 물고기들을 지나갈 수 없는 경우 고려
                    # 최소 경로와 비교하여 더 작은 것이 있으면 교체
                    # 같으면 추가
                    # 더 크면 제외
    global N,fish, shark, sea, time, smc, smn, cnt

    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue.append([shark[1], shark[2], 0])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0 ,-1]

    while queue:
        sy, sx, count = queue.popleft()

        if sy == y and sx == x:
            if smn > count:
                smc = [[y,x]]
                smn = count
                cnt = 1
                return
            elif smn == count:
                smc.append([y,x])
                cnt += 1
                return

        for i in range(4):
            ssy = sy + dy[i]
            ssx = sx + dx[i]

            if 0<=ssy<N and 0<=ssx<N and visited[ssy][ssx] == False and shark[0] >= sea[ssy][ssx]:
                visited[ssy][ssx] = True
                queue.append([ssy,ssx,count+1])

smc = []
smn = 1000
eat_count = 0

def search_fish():
    global N, fish, shark, sea, time, smc, smn, cnt, eat_count

    smc = []
    smn = 1000
    
    for f in fish:
        if f[0] < shark[0]:
            BFS(f[1], f[2])
        
    if len(smc) == 0:
        return -1 # 먹을 수 있는 물고기가 없는 경우

    else:
        # 먹을 수 있는 물고기들 끼리 거리를 비교하여 최소값의 거리에 있는 물고기가 1마리일 경우
        if cnt == 1:
            time += smn
            sea[shark[1]][shark[2]] = 0
            shark[1] = smc[0][0]
            shark[2] = smc[0][1]
            eat_count += 1
            if eat_count == shark[0]:
                eat_count = 0
                shark[0] += 1
            sea[shark[1]][shark[2]] = 0
        #                                                                       여러마리일 경우 계산
        else:
            smc.sort(key=lambda user:(user[0], user[1]))
            time += smn
            sea[shark[1]][shark[2]] = 0
            shark[1] = smc[0][0]
            shark[2] = smc[0][1]
            eat_count += 1
            if eat_count == shark[0]:
                shark[0] += 1
                eat_count = 0
            sea[shark[1]][shark[2]] = 0
        return 0 # 먹을 수 있는 물고기가 없는 경우 다시 탐색하도록 0을 리턴

while True:
    result = search_fish()

    if result == -1:
        print(time)
        break

    fish = deque()
    for i in range(N):
        for j in range(N):
            if sea[i][j] != 0:
                fish.append([sea[i][j], i, j])    