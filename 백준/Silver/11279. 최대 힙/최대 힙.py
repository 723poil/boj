import sys
from collections import deque

def push(heap, data):
    if len(heap) == 0:
        heap.append(data)
        return
    else:
        child = len(heap)+1
        parent = child // 2
        heap.append(int(0))
        while child > 1:
            if data > heap[int(parent)-1]:
                heap[child-1] = heap[int(parent)-1]
                child = int(parent)
                parent /= 2
            else:
                break
        heap[child-1] = data

def pop(heap):
    if len(heap) == 0:
        return 0

    data = heap[0]

    temp = heap.pop()

    if len(heap) == 0:
        return data
    
    parent = 1
    child = parent * 2
    while child <= len(heap):
        if child+1 <= len(heap) and heap[child-1] < heap[child]:
            child += 1
        if heap[child-1] < temp:
            break
        heap[parent - 1] = heap[child-1]
        parent = child
        child *= 2
    heap[parent-1] = temp

    return data

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    heap = deque()

    for i in range(N):
        a = int(sys.stdin.readline())
        if a == 0:
            print(pop(heap))
        else:
            push(heap, a)