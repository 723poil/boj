import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def R(array):
    i = 0
    j = len(array)-1

    while i<j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i+=1
        j-=1

def Dl(array):
    array.popleft()

def Dr(array):
    array.pop()

for _ in range(T):
    p = deque(str(input()))
    n = int(input())
    ac = input().rstrip(']\n').lstrip('[')

    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
    else:
        AC = deque(map(int, ac.split(',')))

        iserror = False

        rcount = 0
        rcountsum = 0
        isl= True
        for i in p:
            if i == '\n':
                continue
            elif i == 'R':
                rcount += 1
                rcountsum += 1
            else:
                if len(AC)==0:
                    iserror = True
                    break
                if rcount % 2 == 0 and isl == True:
                    rcount = 0
                    Dl(AC)
                elif rcount % 2 == 0 and isl == False:
                    rcount = 0
                    Dr(AC)
                elif rcount % 2 == 1 and isl == True:
                    isl = False
                    rcount = 0
                    Dr(AC)
                else:
                    isl = True
                    rcount = 0
                    Dl(AC)

        if rcountsum % 2 != 0:
            R(AC)

        if iserror == False:
            print('[', end='')
            for i in range(len(AC)-1):
                print(AC[i], end=',')
            if len(AC)-1 >= 0:
                print(AC[len(AC)-1], end=']\n')
            else:
                print(']')
        else:
            print('error')
        