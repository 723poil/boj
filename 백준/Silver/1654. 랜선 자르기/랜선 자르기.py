import sys
sys.setrecursionlimit(100000)

K, N = map(int, input().split())

lan = []

for _ in range(K):
    lan.append(int(input()))

def bs (min, max, T):
    global K, N, lan

    mid = (max + min) // 2

    if mid == min:
        return max

    sum = 0
    for i in lan:
        sum += i // mid

    if sum > N and T == False:
        return bs(mid, max, False)
    elif sum < N and T == False:
        return bs(min, mid, False)
    else:
        if sum == N:
            return bs(mid, max, True)
        else:
            return mid

a = bs(0, sum(lan) // N, False)

for i in range(a, 0, -1):
    sum = 0
    for j in lan:
        sum += j // i
    
    if sum >= N:
        print(i)
        break