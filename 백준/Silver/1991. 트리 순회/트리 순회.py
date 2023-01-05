import sys

input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

tree = [Node(i) for i in range(N)]

for i in range(N):
    a, b, c = map(str, input().split(' '))

    if b != '.':
        tree[int(ord(a)-ord('A'))].leftChild = tree[int(ord(b) - ord('A'))]
    if c != '.\n':
        tree[int(ord(a)-ord('A'))].rightChild = tree[int(ord(c[0]) - ord('A'))]

def preorder(ptr):
    if ptr:
        print(chr(ptr.data + ord('A')), end='')
        preorder(ptr.leftChild)
        preorder(ptr.rightChild)

def inorder(ptr):
    if ptr:
        inorder(ptr.leftChild)
        print(chr(ptr.data + ord('A')), end='')
        inorder(ptr.rightChild)

def postorder(ptr):
    if ptr:
        postorder(ptr.leftChild)
        postorder(ptr.rightChild)
        print(chr(ptr.data + ord('A')), end='')

preorder(tree[0])
print()
inorder(tree[0])
print()
postorder(tree[0])