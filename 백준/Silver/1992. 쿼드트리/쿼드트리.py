import sys

input = sys.stdin.readline

def quadtree(starty, endy, startx, endx):
    global N, pixel, answer

    first = pixel[starty][startx]

    for i in range(starty, endy+1):
        for j in range(startx, endx+1):
            if first != pixel[i][j]:
                gap = (endy - starty) // 2 + 1
                print('(', end='')
                quadtree(starty, endy - gap, startx, endx - gap)
                quadtree(starty, endy - gap, startx + gap, endx)
                quadtree(starty + gap, endy, startx, endx - gap)
                quadtree(starty + gap, endy, startx + gap, endx)
                print(')', end='')
                return

    print(first, end='')       
    return

N = int(input())

pixel = ['0']

for i in range(1, N+1):
    a = list(str(input()))
    pixel.append(a)
    pixel[i].insert(0, '0')

quadtree(1, N, 1, N)