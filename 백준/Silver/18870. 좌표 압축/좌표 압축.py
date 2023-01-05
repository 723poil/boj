import sys
from collections import deque

N = int(sys.stdin.readline())
coor_sorted = list(map(int, sys.stdin.readline().rstrip().split()))
coor = coor_sorted.copy()
coor_sorted.sort()
rank = dict()
s = 0

for i in range(N):
    if i == 0:
        rank.update({coor_sorted[i]:s})
        s += 1
    elif coor_sorted[i] == coor_sorted[i-1]:
        continue
    else:
        rank.update({coor_sorted[i]:s})
        s += 1

for i in range(N):
    print(rank.get(coor[i]), end=' ')