import sys

input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

def factorial(n):
    r = 1
    for i in range(2, n+1):
        r = (r * i) % p
    
    return r

def square(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    
    tmp = square(n, k // 2)
    
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p
    
top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

print((top % p) * (square(bot, p-2) % p) % p)