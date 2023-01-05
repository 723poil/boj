# queue의 경우 pop할 경우 뒤의 원소들을 앞으로 땡겨오기 때문에 시간복잡도가 다름

from collections import deque

N = int(input())

Nqueue = deque()

for i in range(N):
    Nqueue.append(i+1)

a = 0
while len(Nqueue) > 1:
    Nqueue.remove(Nqueue[0])
    a = Nqueue.popleft()
    Nqueue.append(a)

print(Nqueue[0])