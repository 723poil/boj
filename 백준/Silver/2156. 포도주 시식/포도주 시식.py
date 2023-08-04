import sys

input = sys.stdin.readline

n = int(input())

wine = [int(input()) for _ in range(n)]

d = [0] * (n+1)

d[0] = wine[0]
if n > 1:
    d[1] = wine[0] + wine[1]
if n > 2:
    d[2] = max(d[1], wine[0] + wine[2], wine[1] + wine[2])

if n > 3:
    for i in range(3, n):
        d[i] = max(d[i-1], wine[i] + d[i-2], wine[i] + wine[i-1] + d[i-3])
    
print(max(d))