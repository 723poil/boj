import sys

input = sys.stdin.readline

T = int(input())

def factorial(a):
    sum = 1
    
    for i in range(1, a+1):
        sum *= i
    
    return sum

for _ in range(T):
    W, E = map(int, input().split())
    
    print(factorial(E) // ( factorial(E-W) * factorial(W)))