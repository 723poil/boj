from collections import deque
N,K = map(int, input().split())

count = 0

def BFS (start, end, count): # BFS로 최단경로 구하기
    visited = [0] * 100001
    queue = deque()

    queue.append((start, count)) # count를 같이 넣어줘야 최단거리를 구할수 있음!
    visited[start] = 1

    while queue:
        a = queue.popleft()
        s, c = a[0], a[1]

        c += 1
        
        for i in range(3):       # 하나의 수에 대한 3가지 경우의 수를 구하기
            plusa = s

            if i == 0:
                plusa -= 1
            elif i == 1:
                plusa += 1
            else:
                if plusa > end:
                    continue
                plusa *= 2

            if plusa == end:     # 원하던 수가 나올 경우 리턴
                return c
            
            if plusa >= 0 and plusa <= 100000:     # 제한된 범위 안에 아직 가지 않은 경로일 경우 queue에 넣기
                if not visited[plusa]:
                    visited[plusa] = 1
                    queue.append((plusa, c))

if N == K:
    print(0)
elif N > K:
    print(N-K)
else:
    print(BFS(N, K, count))