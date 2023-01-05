N = int(input())

e = 1
i = N

while i >= 10:
    i /= 10
    e += 1

errorvalue = e * 9

for j in range(N-errorvalue, N):
    sum = j
    default = j
    temp = int(10)
    while default > 0:
        sum += default % temp
        default //= temp

    if sum == N:
        print(str(j))
        break
    elif j == N-1:
        print(str(0))