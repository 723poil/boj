def Hanoi (n, first, second, third):
    if n==1:
        print(str(first)+ ' ' + str(third))
    else:
        Hanoi(n-1, first, third, second)
        Hanoi(1, first, second, third)
        Hanoi(n-1, second, first, third)

N = int(input())
print(str(int(pow(2, N))-1))
Hanoi(N, 1, 2, 3)
