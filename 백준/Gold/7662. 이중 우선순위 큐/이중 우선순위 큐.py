import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    maxh = []
    minh = []
    visited = [False for _ in range(1000001)]
    for i in range(k):
        a,b = map(str, input().split())

        if a == 'I':
            heapq.heappush(minh, (int(b), i))
            heapq.heappush(maxh, (int(b) *-1, i))
            visited[i] = True
        else:
            if int(b) == 1:
                while maxh and visited[maxh[0][1]] == False:
                    heapq.heappop(maxh)
                
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            else:
                while minh and visited[minh[0][1]] == False:
                    heapq.heappop(minh)
                
                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)

    while maxh and visited[maxh[0][1]] == False:
        heapq.heappop(maxh)
    while minh and visited[minh[0][1]] == False:
        heapq.heappop(minh)

    if maxh and minh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')
