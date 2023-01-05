import sys

input = sys.stdin.readline

s = [1, 1, 1, 2, 2]

T = int(input())

for _ in range(T):
    n = int(input())
    if len(s) >= n:
        print(s[n-1])
    else:
        i = len(s)-1
        while True:
            s.append(s[i] + s[i-4])
            i += 1
            if len(s) == n:
                print(s[n-1])
                break