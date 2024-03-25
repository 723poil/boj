from sys import stdin
from collections import deque

input = stdin.readline

def find_finish(maps: list, pos: tuple):
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]
    
    n, m = pos
    
    searched = [[False for _ in range(m)] for _ in range(n)]
    searched_broken = [[False for _ in range(m)] for _ in range(n)]
    
    qq = deque()
    
    qq.append(((0,0), 1, False))
    searched[0][0] = True
    
    while qq:
        cp, cc, cb = qq.popleft()
        
        if cp[0] == n-1 and cp[1] == m-1:
            return cc
        
        for i in range(4):
            curx = cp[1] + x[i]
            cury = cp[0] + y[i]
            
            able_pos = 0 <= curx < m and 0 <= cury < n
            
            if able_pos and not searched[cury][curx]:
                if cb:
                    if maps[cury][curx] == 0 and not searched_broken[cury][curx]:
                        searched_broken[cury][curx] = True
                        qq.append(((cury, curx), cc + 1, cb))
                else:
                    if maps[cury][curx] == 0:
                        searched[cury][curx] = True
                        qq.append(((cury, curx), cc + 1, cb))
                    else:
                        searched[cury][curx] = True
                        qq.append(((cury, curx), cc + 1, True))
        
    return -1

def solution():
    N, M = map(int, input().split())
    
    maps = []
    
    for _ in range(N):
        maps.append(list(map(int, list(str(input().strip())))))
        
    return find_finish(maps, (N, M))

print(solution())