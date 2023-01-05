import sys

input = sys.stdin.readline

N = int(input())

set = [0] * 21

def add(x):
    global set

    if set[x] == 0:
        set[x] = 1

def remove(x):
    global set

    if set[x] == 1:
        set[x] = 0

def check(x):
    global set

    if set[x] == 1:
        return 1
    else:
        return 0

def toggle(x):
    global set

    if set[x] == 1:
        set[x] = 0
    else:
        set[x] = 1

def all():
    global set

    for i in range(1, 21):
        set[i] = 1

def empty():
    global set
    global zeroset

    for i in range(1, 21):
        set[i] = 0

for _ in range(N):
    a = str(input())

    if a[0] == 'a':
        if a[1] == 'd': # add 함수
            add(int(a[4:]))
        else:           # all 함수
            all()
    elif a[0] == 'r':   # remove 함수
        remove(int(a[7:]))
    elif a[0] == 'c':   # check 함수
        print(check(int(a[6:])))
    elif a[0] == 't':   # toggle 함수
        toggle(int(a[7:]))
    else:               # empty 함수
        empty()
