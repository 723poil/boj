import sys

input = sys.stdin.readline

N = int(input())

paper = [0]

for i in range(1,N+1):
    paper.append(list(map(int,input().split())))
    paper[i].insert(0, 0)

count0 = 0
countm1 = 0
count1 = 0

def paper_count(startx, starty, endx, endy):
    global paper, count0, countm1, count1
    isequal = paper[starty][startx]

    for i in range(starty, endy+1):
        for j in range(startx, endx+1):
            if paper[i][j] != isequal:
                a = (endx+1 - startx) // 3
                paper_count(startx,starty, startx + a - 1, starty + a - 1)                 # 1
                paper_count(startx + a,starty, startx + 2 * a - 1, starty + a - 1)         # 2
                paper_count(startx + 2 * a,starty, endx, starty + a - 1)                   # 3
                paper_count(startx,starty + a, startx + a - 1, starty + 2 * a - 1)         # 4
                paper_count(startx + a,starty + a, startx + 2 * a - 1, starty + 2 * a - 1) # 5
                paper_count(startx + 2 * a,starty + a, endx, starty + 2 * a - 1)           # 6
                paper_count(startx,starty + 2 * a, startx + a - 1, endy)                   # 7
                paper_count(startx + a,starty + 2 * a, startx + 2 * a - 1, endy)           # 8
                paper_count(startx + 2 * a,starty + 2 * a, endx, endy)                     # 9

                return

    if isequal == 0:
        count0 += 1
    elif isequal == -1:
        countm1 += 1
    else:
        count1 += 1
    
paper_count(1, 1, N, N)

print(countm1)
print(count0)
print(count1)