import sys
sys.setrecursionlimit(100000)

def find(a, parent):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a], parent)
    return find(parent[a], parent)

def union(a, b, parent):
    aroot = find(a, parent)
    broot = find(b, parent)

    if aroot <= broot:
        parent[broot] = aroot
    else :
        parent[aroot] = broot

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    parent = dict()

    for i in range(M):
        a = list(map(int, sys.stdin.readline().split()))

        if a[1] not in parent:
            parent[a[1]] = a[1]
        if a[2] not in parent:
            parent[a[2]] = a[2]

        if a[0] == 0:
            union(a[1], a[2], parent)
        elif a[0] == 1:
            if find(a[1], parent) == find(a[2], parent):
                print('YES')
            else :
                print('NO')