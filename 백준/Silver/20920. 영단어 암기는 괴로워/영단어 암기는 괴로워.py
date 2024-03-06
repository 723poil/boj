import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    dt = defaultdict(int)
    
    for _ in range(N):
        tmp = str(input().rstrip())
        
        if len(tmp) < M:
            continue
        
        dt[tmp] += 1
        
    return sorted(list(dt.items()), key= lambda x: (-x[1], -len(x[0]), x[0]))
    
result = solution()
    
for rst in result:
    print(rst[0])