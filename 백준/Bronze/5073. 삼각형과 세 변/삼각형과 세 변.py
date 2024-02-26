import sys

input = sys.stdin.readline

def match(a, b, c):
    if (a + b <= c or a + c <= b or b + c <= a):
        return 'Invalid'
    
    if (a == b == c):
        return 'Equilateral'
    
    if (a == b or b == c or a == c):
        return 'Isosceles'
    
    return 'Scalene'
    

while True:
    a, b, c = map(int, input().split())
    
    if (a == 0 or b == 0 or c == 0):
        break

    print(match(a, b, c))
    

