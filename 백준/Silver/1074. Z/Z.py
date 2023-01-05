import sys
import math
sys.setrecursionlimit(100000)

N,r,c = map(int, input().split())
count = 0

def Z (n, sr, sc, a, na, nb):
    global count
    global r, c
    if n != 2:
        n = int(n / 2)
        if a == 2:    
            nb = nb + n
        elif a == 3:    
            na = na + n
        elif a == 4:
            na = na + n
            nb = nb + n

        if r+1 <= na:
            if c+1 <= nb:
                na -= int(n/2)
                nb -= int(n/2)
                Z(n,sr,sc, 1,na,nb)
            else:
                na -= int(n/2)
                count += n*n
                sc = sc + n
                Z(n,sr,sc, 2,na,nb)
        else:
            count += n*n
            sr = sr + n
            if c+1 <= nb:
                nb -= int(n/2)
                count += n * n
                Z(n,sr,sc, 3,na,nb)
            else:
                count += 2 * n * n
                sc = sc + n
                Z(n,sr,sc, 4,na,nb) 
    else:
        for i in range(4):
            if i == 1:
                sc = sc + 1
            elif i == 2:
                sc = sc - 1
                sr = sr + 1
            elif i == 3:
                sc = sc + 1

            if sr == r+1 and sc == c+1:
                print(count)
                return
            
            count += 1
                
Z(int(pow(2, N)), 1, 1, 1, int(pow(2, N)/2), int(pow(2, N)/2))