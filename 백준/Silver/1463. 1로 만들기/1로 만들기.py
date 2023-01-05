def dp(solve):
    global count
    count += 1
    Nsolve = []
    for a in solve:
        Nsolve.append(a-1)
        if a%3== 0 and a >= 3:
            Nsolve.append(a/3)
        if a%2== 0 and a >=2:
            Nsolve.append(a/2)
    
    return Nsolve

if __name__ == '__main__':
    N = int(input())
    solve = [N]
    count = 0
    if N == 1:
        print(count)
    else:
        while min(solve) != 1:
            solve = dp(solve)

        print(count)