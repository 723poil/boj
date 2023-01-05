N = list(map(int, input().split()))

isbool = False
if N[0] == 1:
    a = sorted(N)
    for i in range(len(N)):
        if a[i] != N[i]:
            isbool = True
            print('mixed')
            break
    if isbool == False:
        print('ascending')
elif N[0] == 8:
    a = 8
    for i in range(len(N)):
        if N[i] != a:
            isbool = True
            print('mixed')
            break
        a -= 1
    if isbool == False:
        print('descending')
else:
    print('mixed')
