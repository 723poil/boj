import sys

N = int(sys.stdin.readline())

if N < 5:
    if N % 3 == 0:
        print(1)
    else:
        print(-1)
else :
    if N % 5 == 0:
        print(int(N / 5))
    else :
        five = N // 5
        three = (N - five*5) // 3
        while True:
            if (N- five*5) % 3 == 0:
                print(five + three)
                break
            else :
                five -= 1
                three = (N-five*5) // 3
                if five < 0:
                    print(-1)
                    break