while True:
    N = str(input())

    if len(N) == 1 and int(N[0]) == 0:
        break

    i=0
    j= len(N)-1
    while i < j:
        if int(N[i]) != int(N[j]):
            print('no')
            break
        i += 1
        j -= 1
    
    if i >= j:
        print('yes')
    