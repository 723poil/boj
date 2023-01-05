T=int(input())

for _ in range(T):
    H, W, N = map(int, input().split())


    h = N % H
    w = N // H
    if h == 0:
        h = H
    if N % H > 0:
        w = 1 + N // H

    if w < 10:
        print(str(h) + '0' + str(w))
    else:
        print(str(h) + str(w))
    # else:
    #     if N % 2 == 0:


    
