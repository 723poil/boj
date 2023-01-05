import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

search = deque(map(int, sys.stdin.readline().split()))
search_position = deque([search[i] for i in range(M)])

queue = deque([i for i in range(1, N+1)])

count = 0
while len(search) > 0:
    if search[0] == queue[0]:
        search.popleft()
        search_position.popleft()
        queue.popleft()
        for i in range(len(search)):
            search_position[i] -= 1
    elif len(queue)// 2 + 1 >= search_position[0]:
        while queue[0] != search[0]:
            for i in range(len(search)):
                if search_position[i] == 1:
                    search_position[i] = len(queue)+1
                search_position[i] -= 1
            a = queue.popleft()
            queue.append(a)
            count += 1
            
        search.popleft()
        search_position.popleft()
        queue.popleft()
        for i in range(len(search)):
            search_position[i] -= 1
    else:
        while queue[0] != search[0]:
            for i in range(len(search)):
                if search_position[i] == len(queue):
                    search_position[i] = 0
                search_position[i] += 1
            a = queue.pop()
            queue.insert(0, a)
            count += 1
            
        search.popleft()
        search_position.popleft()
        queue.popleft()
        for i in range(len(search)):
            search_position[i] -= 1

print(count)