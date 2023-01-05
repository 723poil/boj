import math

while True:
    a = list(map(int, input().split()))

    if a[0] == a[1] == a[2] == 0:
        break

    a.sort()

    long = int(pow(a[2], 2))
    shorta = int(pow(a[0], 2))
    shortb = int(pow(a[1], 2))
    
    if shorta + shortb == long:
        print('right')
    else:
        print('wrong')
    