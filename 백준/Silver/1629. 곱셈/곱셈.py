A,B,C = map(int, input().split())

def zegob(x, y, z):
    if y == 1:
        return x % z
    else:
        zego = zegob(x, y//2, z)
        if y % 2 == 1:
            return zego * zego % z * x % z
        else:
            return zego * zego % z

print(zegob(A,B,C))