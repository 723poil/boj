import math
import sys

input = sys.stdin.readline

T=int(input())

for _ in range(T):
    n = int(input())

    kc = []
    c = [0] * n
    for _ in range(n):
        a, b = map(str, input().split())
        if b not in kc:
            kc.append(b)
            c[kc.index(b)] += 1
        else:
            c[kc.index(b)] += 1

    sum = 1
    for i in range(len(kc)):
        a = c[i] + 1
        sum *= a

    print(sum-1) 