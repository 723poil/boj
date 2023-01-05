import sys
from collections import deque

N, K = map(int, input().split())

money = deque()

for _ in range(N):
    money.appendleft(int(input()))

count = 0

m = 0

while m != K:
    a = money.popleft()

    if a > K - m:
        continue
    else:
        count += (K - m) // a
        m += ((K - m) // a) * a

print(count)