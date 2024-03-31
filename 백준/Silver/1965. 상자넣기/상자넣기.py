from sys import stdin

input = stdin.readline

def solution():
    n = int(input())
    boxes = list(map(int, input().split()))
    box_count = [1 for _ in range(n)]
    
    for i in range(1, n):
        max_count = max([box_count[j] if boxes[j] < boxes[i] else 0 for j in range(i, -1, -1)])
        
        box_count[i] += max_count
            
    return sorted(box_count, key= lambda x: -x)[0]
    
print(solution())