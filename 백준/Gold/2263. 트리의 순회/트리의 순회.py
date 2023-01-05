import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index = [-1 for _ in range(N+1)]
for i in range(N):
    index[inorder[i]] = i

def retrival(starti, endi, posi, poei): 
    
    if starti > endi and posi > poei:
        return

    print(postorder[poei], end=' ')
    j = index[postorder[poei]]
    size = j - starti

    retrival(starti, j-1, posi, posi+size-1)
    retrival(j+1, endi, posi+size, poei-1)
retrival(0, N-1, 0, N-1)