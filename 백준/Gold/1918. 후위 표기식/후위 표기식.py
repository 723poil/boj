import sys
from collections import deque

input = sys.stdin.readline

operator = ['+', '-', '*', '/']
bracket = ['(', ')']
inorder = deque(input().rstrip('\n'))

stack = []
postfix = []

def pref(o):
    if o == '*' or o == '/':
        return 1
    elif o == '+' or o == '-':
        return 0
    else:
        return -1

while inorder:
    op = inorder.popleft()

    if op not in operator and op not in bracket:
        postfix.append(op)
    elif op in operator:
        pre = pref(op)

        while stack:
            if pref(stack[-1]) < pre:
                break
            postfix.append(stack.pop())
        stack.append(op)
    elif op == '(':
        stack.append(op)
    elif op == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()

while stack:
    postfix.append(stack.pop())

s = "".join(postfix)

print(s)