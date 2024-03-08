import sys
from collections import Counter

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    total = int(input())
    
    answer = 0
    
    arr.sort()
    for i in range(N):
        if (total // (N - i)) <= arr[i]:
            return total // (N - i)
        
        answer = arr[i]
        total -= arr[i]
        
    return answer
    
result = solution()

print(result)