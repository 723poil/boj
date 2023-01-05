import sys

N, M = map(int, sys.stdin.readline().split())
r, c, dir = map(int, sys.stdin.readline().split())
space = [[0]*M for _ in range(N)]
isclean = [[0]*M for _ in range(N)]

count = 0

def dircount(ra, ca, dira):
    global space , r, c, dir
    for _ in range(4):
        dira = dira - 1
        if dira < 0 :
            dira = 3

        if dira == 0:
            if isclean[ra-1][ca] == 0 and space[ra-1][ca] != 1:
                isclean[ra-1][ca] = 1
                r = r-1
                dir = dira
                return 1
        elif dira == 1:
            if isclean[ra][ca+1] == 0 and space[ra][ca+1] != 1:
                isclean[ra][ca+1] = 1
                c = c+1
                dir = dira
                return 1
        elif dira == 2:
            if isclean[ra+1][ca] == 0 and space[ra+1][ca] != 1:
                isclean[ra+1][ca] = 1
                r = r+1
                dir = dira
                return 1
        elif dira == 3:
            if isclean[ra][ca-1] == 0 and space[ra][ca-1] != 1:
                isclean[ra][ca-1] = 1
                c = c-1
                dir = dira
                return 1

    if dir == 0 :
        if space[ra+1][ca] == 1:
            return -1
        else:
            r = r+1
    elif dir == 1:
        if space[ra][ca-1] == 1:
            return -1
        else:
            c = c-1
    elif dir == 2:
        if space[ra-1][ca] == 1:
            return -1
        else:
            r = r-1
    elif dir == 3:
        if space[ra][ca+1] == 1:
            return -1
        else:
            c = c+1

    return 0




if __name__ == '__main__':
    for i in range(N):
        space[i] = list(map(int, sys.stdin.readline().split()))
    
    while True:
        count += 1
        if isclean[r][c] == 0:
            isclean[r][c] = 1
        
        a = dircount(r,c,dir)
        if a == -1:
            print(count)
            break
        elif a == 0:
            count -= 1


