from collections import deque

N, K = map(int, input().split())

josephus_list = deque(range(1, N+1))
i = K-1
print('<'+str(josephus_list[i]), end= '')
josephus_list.remove(josephus_list[i])
N -= 1
while len(josephus_list) > 0:
    i = (i+K-1) % N
    print(', '+str(josephus_list[i]), end = '')
    josephus_list.remove(josephus_list[i])
    N -= 1

print('>')
