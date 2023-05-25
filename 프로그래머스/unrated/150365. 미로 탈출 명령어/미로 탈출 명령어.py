from collections import deque

def solution(n, m, x, y, r, c, k):
    dir = [(1,0,'d'), (0,-1,'l'), (0,1,'r'), (-1,0,'u')]
    
    queue = deque()
    queue.append([x, y, 0, ""])
    
    while queue:
        x_1, y_1, k_1, s = queue.popleft()
        
        if k_1 == k and (x_1, y_1) == (r, c):
            return s
        if (x_1, y_1) == (r, c) and (k-k_1) % 2 == 1:
            return "impossible"
        
        for i in range(4):
            dx, dy, ds = dir[i]
            dx += x_1
            dy += y_1
            ds = s + ds
            if 0 < dx < n+1 and 0 < dy < m+1:
                check_imp = abs(r-dx) + abs(c-dy)
                re_k = k - (k_1 + 1)
                if check_imp <= re_k:
                    queue.append([dx, dy, k_1 + 1, ds])
                    break
    
    return "impossible"