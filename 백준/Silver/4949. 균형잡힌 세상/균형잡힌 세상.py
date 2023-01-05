import sys
from collections import deque

con = True

while con:
    string = sys.stdin.readline()
    if string == '.\n':
        con = False
        break

    balance = deque()
    balance_count = 0

    for i in range(len(string)):
        if string[i] == '(':
            balance.append('(')
        elif string[i] == '[':
            balance.append('[')
        elif string[i] == ')' :
            if len(balance) > 0 and balance[len(balance)-1] == '(' : 
                balance.pop()
            else :
                print('no')
                break
        elif string[i] == ']':
            if len(balance) > 0 and balance[len(balance)-1] == '[': 
                balance.pop()
            else:
                print('no')
                break
        
        if i == len(string)-1 and len(balance) == 0:
            print('yes')
        elif i == len(string)-1 :
            print('no')