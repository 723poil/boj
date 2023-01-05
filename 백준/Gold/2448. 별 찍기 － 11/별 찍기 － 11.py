import sys
sys.setrecursionlimit(10**6)
N = int(input())

stars = [[' '] * (5 * (N//3) + (N//3)-1) for _ in range(N)]

def star(sl, n, part, jump):
    if part == 0:
        # n == 3
        if n == 3:
            a = 0
        # n == 6
        elif n == 6:
            a = 3
        # 나머지
        else:
            a = (n//3) // 4 + (5 * (n//3) // 4)
        
        if a == 0:
            star(sl, n, 1, jump)
            return

        star(sl, n//2, 0, jump)
        star(sl+n//2, n//2, 0, jump)
        star(sl+n//2, n//2, 0, jump + 2 * a)
        
    else:
        stars[sl][jump] = '*'
        stars[sl+1][jump] = '*'
        stars[sl+1][jump+2] = '*'

        for i in range(jump, jump+5):
            stars[sl+2][i] = '*'

star(0, N, 0, 0)

space = N-1
count = 1

for i in range(N):
    print(' '*space, end='')
    print(''.join(stars[i][:count]), end='')
    print(' '*space)

    space -= 1
    count += 2