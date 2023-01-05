import sys
from collections import deque

def push(data):
    global queue

    queue.append(data)

def pop():
    global queue
    if len(queue) == 0:
        return -1
    data = queue.popleft()
    return data

def size():
    global queue

    return len(queue)

def empty():
    global queue

    if len(queue) == 0:
        return 1
    return 0

def front():
    global queue
    if len(queue) == 0:
        return -1
    return queue[0]

def back():
    global queue
    if len(queue) == 0:
        return -1
    return queue[len(queue)-1]


queue = deque()

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for i in range(N):
        a = sys.stdin.readline().rstrip().split(' ')
        b = a[0]

        if b == 'push':
            push(a[1])
        elif b == 'pop':
            print(pop())
        elif b == 'size':
            print(size())
        elif b == 'empty':
            print(empty())
        elif b == 'front':
            print(front())
        elif b == 'back':
            print(back())