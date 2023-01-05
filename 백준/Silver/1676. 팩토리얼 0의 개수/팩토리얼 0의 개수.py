N = int(input())

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

N_str = list(str(factorial(N)))

count = 0
while N_str[-1] == '0':
    N_str.pop()
    count += 1

print(count)