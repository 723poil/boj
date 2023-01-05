import sys
from collections import deque

class node:
    def __init__(self, data, previous=None, next=None):
        self.previous = previous
        self.next = next
        self.data = data
        if previous != None:
            previous.next = self
        if next != None:
            next.previous = self

class linkedlist:
    def __init__(self, data):
        self.start = node(data[0])
        self.pointer = self.start
        for i in data[1:]:
            if i != '\n':
                self.pointer = node(i, self.pointer)
        self.pointer = node('end', self.pointer)

    def move(self, m):
        if m == 'L' and self.pointer.previous != None:
            self.pointer = self.pointer.previous
        elif m == 'D' and self.pointer.next != None:
            self.pointer = self.pointer.next

    def remove(self):
        if self.pointer.previous != None and self.pointer.previous.previous != None:
            self.temp = self.pointer.previous.previous
            del self.pointer.previous
            self.pointer.previous = self.temp
            self.temp.next = self.pointer
        elif self.pointer.previous != None:
            del self.pointer.previous
            self.pointer.previous = None
            self.start = self.pointer

    def add(self, data):
        if self.pointer.previous == None:
            self.start = node(data, self.pointer.previous, self.pointer)
        else:
            node(data, self.pointer.previous, self.pointer)

    def get(self):
        self.cur = self.start
        while self.cur.data != 'end':
            print(self.cur.data, end='')
            self.cur = self.cur.next

if __name__ == '__main__':
    L = linkedlist(sys.stdin.readline())
    M = int(sys.stdin.readline())

    for i in range(M):
        a = sys.stdin.readline()
        if a[0] == 'L' or a[0] == 'D':
            L.move(a[0])
        elif a[0] == 'B':
            L.remove()
        elif a[0] == 'P':
            L.add(a[2])
    L.get()

