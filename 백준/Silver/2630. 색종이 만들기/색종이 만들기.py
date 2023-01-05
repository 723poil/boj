import sys

input = sys.stdin.readline

N = int(input())

paper = [[0] for _ in range(N+1)]

for i in range(1, N+1):
    a = list(map(int,input().split()))
    a.insert(0, 0)
    paper[i] = a

white_count = 0
blue_count = 0

def paper_count(startx, endx, starty, endy):
    global white_count, blue_count, paper

    first = paper[starty][startx]

    for i in range(starty, endy+1):
        for j in range(startx, endx+1):
            if first != paper[i][j]:
                gap = (endx - startx + 1) // 2
                paper_count(startx, endx - gap, starty, endy - gap)
                paper_count(startx + gap, endx, starty, endy - gap)
                paper_count(startx, endx - gap, starty + gap, endy)
                paper_count(startx + gap, endx, starty + gap, endy)
                return
            if i == endy and j == endx:
                if first == 1:
                    blue_count += 1
                else:
                    white_count += 1
                return

paper_count(1, N, 1, N)

print(white_count)
print(blue_count)