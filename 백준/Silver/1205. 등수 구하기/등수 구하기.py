import sys

input = sys.stdin.readline

def solution():
    N, T, P = map(int, input().split())
    
    n_arr = []
    
    if N > 0:
        n_arr = list(map(int, input().split()))
        
    # 배열값이 없을때
    if N == 0:
        return 1
    
    # 주어진 배열과 점수 제한이 같을때
    if P == N and n_arr[-1] >= T:
        return -1
    
    # N < P
    cur_rank = 0
    cur_dup = 0
    before_dup = 0
    cur_num = -1
    before_num = -1
    
    for i in range(N):
        
        
        if cur_num != n_arr[i]:
            before_num = cur_num
            cur_num = n_arr[i]
            cur_rank += (1 + cur_dup)
            before_dup = cur_dup
            cur_dup = 0
            
            if cur_num < T and before_num == T:
                return cur_rank - 1 - before_dup
            elif cur_num < T:
                return cur_rank
            
        elif cur_num == n_arr[i]:
            cur_dup += 1
    
    if cur_num == T:
        return cur_rank
    
    return cur_rank+1+cur_dup
        
print(solution())