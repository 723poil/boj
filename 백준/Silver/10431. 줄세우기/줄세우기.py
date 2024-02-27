import sys

input = sys.stdin.readline

def find(x, arr):
    for i in range(len(arr)):
        if x < arr[i]:
            return i
        
    return -1

def sort(arr):
    cnt = 0
    tmp = []
    
    for a in arr:
        idx = find(a, tmp)
        
        if (idx == -1):
            tmp.append(a)
        else:
            cnt += (len(tmp) - idx)
            tmp.insert(idx, a)
            
    return cnt
            
        

P = int(input())

for _ in range(P):
    tmp = list(map(int, input().split()))
    
    T = tmp[0]
    arr = tmp[1:]
    
    print(T, sort(arr))
    
    