import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.insert(0, 0)

P.sort()

sum = 0
n = N

for i in range(1, N+1):
    sum += P[i] * n
    n = n - 1

print(sum)