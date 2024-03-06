import sys
from collections import Counter

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    words = [input().rstrip() for _ in range(N)]
    
    counter = Counter(word for word in words if len(word) >= M)
    
    result = list(counter)
    result.sort()
    result.sort(key=len, reverse=True)
    result.sort(key=counter.get, reverse=True)
    
    return result
    
result = solution()

print("\n".join(result))