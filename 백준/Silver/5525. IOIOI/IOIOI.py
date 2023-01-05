import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input())

st = str('I' * (N+1))
P = 'O'.join(st)

if 2*N + 1 > M:
    print(0)
elif 2*N + 1 == M:
    if S[0] == 'O':
        print(0)
else:
    i = 0
    count = 0
    while i <= M - 2*N + 1:
        if S[i] == 'I' and S[i+1] == 'O' and S[i+2 == 'I']:
            s = ''.join(S[i:i+2*N + 1])
            if s == P:
                count += 1
        
        i += 1
    
    print(count)