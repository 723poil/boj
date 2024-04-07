from sys import stdin

input = stdin.readline

def check_lastest(stack: list, ks_c: list) -> int:
    
    temp = [(i, ks_c[i][0] if len(ks_c[i]) != 0 else 999, 0 if i in stack else 999) for i in range(1, len(ks_c))]
    
    temp.sort(key= lambda x: (x[2], -x[1]))

    return stack.index(temp[0][0])   

def optimal_method(N: int, K: int, ks: list, ks_c: list) -> int:
    
    stack = []
    count = 0
    
    for i in range(K):
        # 이미 꽂혀있으면 넘어가기
        if ks[i] in stack:
            ks_c[ks[i]].pop(0)
            continue
        
        # 플러그 남았을때 그냥 꽂기
        if len(stack) < N:
            stack.append(ks[i])
            ks_c[ks[i]].pop(0)
            continue
        
        index = check_lastest(stack, ks_c)
        ks_c[ks[i]].pop(0)
        stack[index] = ks[i]
        
        count += 1    
            
    return count

def solution():
    N, K = map(int, input().split())
    
    ks = list(map(int, input().split()))
    ks_c = [[] for _ in range(K+1)]
    
    for k in range(K):
        ks_c[ks[k]].append(k)
    
    return optimal_method(N, K, ks, ks_c)

print(solution())