import sys
import heapq

input = sys.stdin.readline

N=int(input())

ah = []

for i in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(ah, (abs(x), x, i))
    else:
        if ah:
            print(heapq.heappop(ah)[1])
        else:
            print(0)
    