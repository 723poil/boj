N, K = map(int, input().split())

def factorial(a):
    if a == 0 :
        return 1
    elif a == 1 :
        return 1
    else:
        return factorial(a-1) * a

b = factorial(N) / (factorial(K) * factorial(N-K))

print(int(b))